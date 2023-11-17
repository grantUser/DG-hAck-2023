# DG-hAck-2023 Feed This Dragon

### Challenge Explanation

For "Feed This Dragon," the provided Python script automates the clicking on positive items in a game using concurrent threads. The script interacts with an API, attempting to click on various items such as "life," "bigboo," "midboo," "lilboo," "food," "veggy," "candy," "burger," "gem," "coin," "secret," "nyan."

### Flag Explanation

The flag for Feed This Dragon is **DGHACK{ThisDragonIsNowStuffed}**. This flag is a unique identifier associated with the successful completion of the challenge. It serves as proof that the automation script has effectively interacted with the game's API and fulfilled the challenge requirements.

### Instructions for Optimization

To enhance the script, consider modifying the automation logic to click on all items except the negative ones. This can be achieved by adjusting the conditions in the script to exclude items labeled as "negative."

Additionally, pay attention to items such as "secrets" and "nyan" that are not visible without achieving specific successes. Adjust the script to account for these specific conditions and automate the clicks accordingly.

**Note:** The script does not automate clicks in the shop, as it is not deemed necessary. Manual parallel clicking in the browser is considered an easy alternative.

# Infinite Money Glitch Challenge

### Challenge Explanation

Introducing the "Infinite Money Glitch" challenge. This challenge focuses on exploiting a glitch to generate infinite money within the game.

### Flag Explanation

The flag for the Infinite Money Glitch Challenge is **DGHACK{ButWhereCanIActuallySpendIt}**. This flag serves as proof that the glitch has been successfully exploited, allowing the player to accumulate infinite money.

### Resolution Insight

During the investigation, it was observed that the video links were unique but that the videos themselves were reused. By applying optical character recognition (OCR) to each video and caching each code via the hash of the video we were able to generate enough currency to promote the new accounts (€50 instead of €500). 

An .ipynb to be used in Google Collab has been made available as proof.

### Additional Insights

Contributors may provide additional insights or improvements to the solution. Suggestions for optimizing the code, handling edge cases, or incorporating new features are welcome.

Good luck with your further challenges!
