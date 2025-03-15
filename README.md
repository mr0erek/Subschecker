# Subschecker
>[!NOTE]
> This PROJECT needs a valid api of google YT Channel stats, Beause It needs a valid reason and proper documentation for API creation and it's usage.
> As I have no such valid reason with it's docs, This Project is now Archived by myside, sooner I will create docs related to it and upstream this project later.

> Till then if you want to create your own API using this, Simply Generate API key from Google and Follow Bellow Steps:
>  1. While Deploying this Project on vercel You need to add Environment variable with it's value like  `CLIENT_ID` : `<YOUR_API_KEY>` and `CLIENT_SECRET` : `Unique_KEY`

>  `CLIENT_SECRET` is just to encrypted data, you can put anything (e.g. : `CLIENT_SECRET` = "`ABCD@1234`") Keep It Strong for better encryption
### Purpose of the App: 
 - Our app, the YouTube Subscriber Status Checker, is designed to access a user’s YouTube subscription status for a specific channel using the YouTube API. The purpose is solely to create a real-time API-based project, primarily as a portfolio piece to showcase technical skills in API integration and OAuth2 implementation within a secure, user-centered application environment. This app will help demonstrate proficiency in working with third-party APIs in my resume and professional profile.
### Why Access is Needed: 
 - To accurately and securely validate a user’s subscription status, the app requires access to the youtube.readonly scope. This access allows the app to read basic subscriber information without modifying user data. By using this sensitive scope, the app can demonstrate real-world capabilities in handling OAuth2 flows, ensuring secure access to restricted data, and implementing best practices in user authentication and permissions handling.
### Privacy and Data Usage: 
 - The app does not store or share any user data. It is solely for personal project purposes to exhibit API interaction skills, and the app only requests the minimum scope needed to check the subscription status. A detailed Privacy Policy has been created to assure users that no personal data is stored or retained.
