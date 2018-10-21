## Google Play:
### googleplaystore.csv
- App: Application name
- Category: Category the app belongs to ss
- Rating: Overall user rating of the app (as when scraped)
- Reviews: Number of user reviews for the app (as when scraped)
- Size: Size of the app (as when scraped)
- Installs: Number of user downloads/installs for the app (as when scraped)
- Type: Paid or Free
- Price: Price of the app (as when scraped)
- Content Rating: Age group the app is targeted at - Children / Mature 21+ / Adult
- Genres: An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.
- Last Updated: Date when the app was last updated on Play Store (as when scraped)
- Current Ver: Current version of the app available on Play Store (as when scraped)
- Android Ver: Min required Android version (as when scraped)

### googleplaystore_user_reviews.csv
- App: Name of app
- Translated_Review: User review (Preprocessed and translated to English)
- Sentiment: Positive/Negative/Neutral (Preprocessed)
- Sentiment_Polarity: Sentiment polarity score
- Sentiment_Subjectivity: Sentiment subjectivity score:

## App Store
### appleStore.csv
- id : App ID
- track_name: App Name
- size_bytes: Size (in Bytes)
- currency: Currency Type
- price: Price amount
- rating_count_tot: User Rating counts (for all version)
- rating_count_ver: User Rating counts (for current version)
- user_rating : Average User Rating value (for all version)
- user_rating_ver: Average User Rating value (for current version)
- ver : Latest version code
- cont_rating: Content Rating
- prime_genre: Primary Genre
- sup_devices.num: Number of supporting devices
- ipadSc_urls.num: Number of screenshots showed for display
- lang.num: Number of supported languages
- vpp_lic: Vpp Device Based Licensing Enabled

### appleStore_description.csv
- id : App ID
- track_name: Application name
- size_bytes: Memory size (in Bytes)
- app_desc: Application description
