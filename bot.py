import discord
from discord.ext import tasks
from pinscrape import scraper, Pinterest
import os
from dotenv import load_dotenv
import shutil
import time
import io

load_dotenv()

EMBED_COLOR = int(os.getenv('EMBED_COLOR', '0x323337'), 16)

# Get cooldown duration from .env (default: 30 seconds)
COOLDOWN_DURATION = int(os.getenv('COOLDOWN_DURATION', '30'))

# Cooldown tracking for users (user_id: last_use_timestamp)
user_cooldowns = {}

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

def cleanup_temp_folders():
    """Clean up any leftover temp folders from previous runs"""
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        if item.startswith('temp_') and os.path.isdir(item):
            try:
                shutil.rmtree(item)
                print(f"Cleaned up leftover folder: {item}")
            except Exception as e:
                print(f"Could not clean up {item}: {e}")

def cleanup_old_cooldowns():
    """Remove cooldown entries older than 1 hour to prevent memory buildup"""
    current_time = time.time()
    expired_users = []
    
    for user_id, last_use in user_cooldowns.items():
        if current_time - last_use > 3600:  # 1 hour
            expired_users.append(user_id)
    
    for user_id in expired_users:
        del user_cooldowns[user_id]
    
    if expired_users:
        print(f"Cleaned up {len(expired_users)} expired cooldown entries")

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')
    cleanup_temp_folders()
    
    # Start periodic cooldown cleanup
    cleanup_cooldowns_task.start()

@discord.ext.tasks.loop(minutes=30)
async def cleanup_cooldowns_task():
    """Periodic cleanup of old cooldown entries"""
    cleanup_old_cooldowns()

@bot.slash_command(name="pull", description="Search and download images from database")
async def pull_images(ctx: discord.ApplicationContext, keyword: str, amount: int = 5, ephemeral: bool = False):
    # Check cooldown (configurable via .env)
    user_id = ctx.author.id
    current_time = time.time()
    cooldown_duration = COOLDOWN_DURATION
    
    if user_id in user_cooldowns:
        time_since_last_use = current_time - user_cooldowns[user_id]
        if time_since_last_use < cooldown_duration:
            remaining_time = int(cooldown_duration - time_since_last_use)
            embed = discord.Embed(
                title="⏰ Cooldown Active",
                description=f"You can use this command again in **{remaining_time}** seconds\n\n*Cooldown: {COOLDOWN_DURATION} seconds*",
                color=EMBED_COLOR
            )
            await ctx.respond(embed=embed, ephemeral=True)
            return
    
    # Update cooldown timestamp
    user_cooldowns[user_id] = current_time
    
    if amount < 1 or amount > 10:
        embed = discord.Embed(
            title="❌ Invalid Amount",
            description="Number must be between 1 and 10! (Discord attachment limit)",
            color=EMBED_COLOR
        )
        await ctx.respond(embed=embed, ephemeral=ephemeral)
        return
    
    # Initial search embed
    embed = discord.Embed(
        title="🔍 Searching Database",
        description=f"Looking for **{keyword}** images...",
        color=EMBED_COLOR
    )
    response = await ctx.respond(embed=embed, ephemeral=ephemeral)
    
    output_folder = f"temp_{ctx.author.id}"
    
    try:
        # Use Pinterest scraper
        p = Pinterest(proxies={}, sleep_time=2)
        images_url = p.search(keyword, amount)
        
        if not images_url:
            embed = discord.Embed(
                title="❌ No Results",
                description=f"No images found for **{keyword}** in database",
                color=EMBED_COLOR
            )
            await response.edit_original_response(embed=embed)
            return
        
        # Download images
        p.download(url_list=images_url, number_of_workers=5, output_folder=output_folder)
        
        # Collect downloaded files with validation
        file_paths = []
        if os.path.exists(output_folder):
            for filename in os.listdir(output_folder):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    file_path = os.path.join(output_folder, filename)
                    try:
                        # Check if file exists and has valid size
                        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                            if os.path.getsize(file_path) < 8 * 1024 * 1024:  # 8MB limit
                                # Try to read first few bytes to validate it's a valid file
                                with open(file_path, 'rb') as test_file:
                                    test_file.read(10)  # Read first 10 bytes
                                file_paths.append(file_path)
                    except Exception as validation_error:
                        print(f"Skipping invalid file {filename}: {validation_error}")
                        continue
        
        if file_paths:
            # Discord allows max 10 attachments per message
            max_files = min(len(file_paths), 10)
            files = []
            
            # Create discord.File objects with proper file handling
            for i in range(max_files):
                try:
                    # Read file content into memory to avoid file handle issues
                    with open(file_paths[i], 'rb') as f:
                        file_data = f.read()
                    
                    # Create BytesIO object for Discord.py
                    file_buffer = io.BytesIO(file_data)
                    filename = os.path.basename(file_paths[i])
                    files.append(discord.File(fp=file_buffer, filename=filename))
                except Exception as file_error:
                    print(f"Error reading file {file_paths[i]}: {file_error}")
                    continue
            
            if files:  # Only send if we have valid files
                await response.edit_original_response(content=None, embed=None, files=files)
            else:
                # No valid files after processing
                embed = discord.Embed(
                    title="❌ Processing Failed",
                    description="Downloaded files could not be processed",
                    color=EMBED_COLOR
                )
                embed.add_field(
                    name="🔧 Possible Issues",
                    value="• Corrupted image files\n• Unsupported file formats\n• Network download errors",
                    inline=False
                )
                await response.edit_original_response(embed=embed)
        else:
            # No valid files embed
            embed = discord.Embed(
                title="❌ Download Failed",
                description="Database found results but couldn't download valid images",
                color=EMBED_COLOR
            )
            embed.add_field(
                name="🔧 Possible Issues",
                value="• Images too large (>8MB)\n• Network connection problems\n• Invalid image formats",
                inline=False
            )
            await response.edit_original_response(embed=embed)
                
    except Exception as e:
        print(f"Error in pull command: {e}")
        
        # Error embed
        embed = discord.Embed(
            title="❌ Database Error",
            description=f"An error occurred while searching the database",
            color=EMBED_COLOR
        )
        embed.add_field(
            name="🐛 Error Details",
            value=f"```\n{str(e)[:100]}...\n```",
            inline=False
        )
        embed.add_field(
            name="💡 Try Again",
            value="• Check your search term\n• Wait a moment and retry\n• Use different keywords",
            inline=False
        )
        await response.edit_original_response(embed=embed)
        
    finally:
        # Always cleanup temp folder with improved error handling
        if os.path.exists(output_folder):
            import gc
            
            # Force garbage collection to release any remaining file handles
            gc.collect()
            
            max_retries = 5
            for attempt in range(max_retries):
                try:
                    # Try to delete individual files first
                    if os.path.exists(output_folder):
                        for filename in os.listdir(output_folder):
                            file_path = os.path.join(output_folder, filename)
                            try:
                                os.remove(file_path)
                            except Exception:
                                pass  # Continue with other files
                        
                        # Then try to remove the folder
                        os.rmdir(output_folder)
                        print(f"Cleaned up folder: {output_folder}")
                        break
                except Exception as e:
                    if attempt < max_retries - 1:
                        print(f"Cleanup attempt {attempt + 1} failed, retrying in 2 seconds...")
                        time.sleep(2)
                    else:
                        print(f"Cleanup error after {max_retries} attempts: {e}")
                        print("Temp folder will be cleaned up on next bot restart")

if __name__ == "__main__":
    bot.run(os.getenv('BOT_TOKEN'))
