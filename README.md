## Task 7 ## 
DAG
![dag](https://user-images.githubusercontent.com/121276417/214596355-4a16a2d7-d76a-4288-a1d0-b0cdaa423152.png)

### 1st query ###

db.tik_tok.find({}, {"_id":0, "content":1, "thumbsUpCount":1, "score":1}).sort({"thumbsUpCount":-1}).limit(5).pretty()

#### Output: ####

{
        "content" : "I love TikTok. However, I've recently had a lot of issues. First, I couldn't use all the filters. I kept getting notifications that the filter couldn't be used on my phone. I can use them all now, but now the captions are messed up. Other reviews say the captions don't show up at all, but I get double captions! It's infuriating. I've tried turning them off under accessibility, but that does nothing.",
        "score" : 3,
        "thumbsUpCount" : 20102
}
{
        "content" : "faxing didn't break any kind of TikTok cummunty guidelines I think someone peoples flagged my videos please review my account again and fix it as soon as possible",
        "score" : 1,
        "thumbsUpCount" : 11380
}
{
        "content" : "Honestly the best app ever created. I love the content. BUT ever since it's updated the videos are slow, the sound carries over from the last video played and keeps replaying, you swipe for the next video and it doesn't play, the lives get stuck on one motion pic. I've restarted my phone, quit the app but I believe it's the app it's self acting weird. I'm not liking it right now.",
        "score" : 1,
        "thumbsUpCount" : 11030
}
{
        "content" : "The app is fun as heck. Many videos give a unique perspective about love, sex, about stress about women about the male perspective. Then there are even political and cop discussions that go on in the comment section. And a lot of the animal videos are fascinating and heartwarming to watch. It's a creative site that keeps changing with new interesting videos added almost every second!",
        "score" : 5,
        "thumbsUpCount" : 10298
}
{
        "content" : "I have reported many times people being very racist and or making fun of my religion, Muslim religion yet this app does not look into it says its not against the guidelines this is sent immediately after I complain. So its OK to make fun of my prophet and its fine? Does not surprise me. Pick and choose what you want to do. You should treat everyone the same.",
        "score" : 1,
        "thumbsUpCount" : 10206
}


### 2nd query ###

db.tik_tok.find({$expr: {$lt: [{ $strLenCP: "$content"}, 5]}}).pretty()

#### Output: ####

{
        "_id" : ObjectId("63d111789ca56cd38aa21748"),
        "reviewId" : "gp:AOqpTOFOKOxBKWDbUjaoQml2UEqeVgQkcZ84CAPnb6QhkhAr4ZPzN7Uk-LEFPiadIkyIdTbTyDPJD68_rnHZKw",
        "userName" : "OmoAkinola Survey Consult",
        "userImage" : "https://play-lh.googleusercontent.com/a-/AOh14GgZoAE7MUU4S-mtwNnYxmOv0AKj_N7qShN2Pn6v",
        "content" : "Cool",
        "score" : 5,
        "thumbsUpCount" : 0,
        "reviewCreatedVersion" : "22.4.5",
        "at" : "2022-01-17 10:46:27",
        "replyContent" : "-",
        "repliedAt" : "-"
}
{
        "_id" : ObjectId("63d111789ca56cd38aa21749"),
        "reviewId" : "gp:AOqpTOHLfvI7OYaoZS7MfhKmAxhzO2e54givQyufirtFYxMTAAW5S2_L1Ye_jrVXhRUQAc5MHqpywG8ahMTO0w",
        "userName" : "S R",
        "userImage" : "https://play-lh.googleusercontent.com/a-/AOh14GjlWnl7eU-O-5vj-GpNH68L91Uh50yK4qcUGXIM",
        "content" : "Best",
        "score" : 5,
        "thumbsUpCount" : 0,
        "reviewCreatedVersion" : "-",
        "at" : "2022-01-17 10:46:40",
        "replyContent" : "-",
        "repliedAt" : "-"
}
{
        "_id" : ObjectId("63d111789ca56cd38aa2174f"),
        "reviewId" : "gp:AOqpTOHTMZ5SKFjBKouf9AAlILutA9cpvcTIq-HuIKJ2zkEgoToIANqxMrKrpIdjqhnO4j-9_CRqiq0w4RY_XQ",
        "userName" : "Mizan Maji",
        "userImage" : "https://play-lh.googleusercontent.com/a/AATXAJzSTlQPRX27O4syQ4e7h9g0Rxl9BLLyiz14Ewnm=mo",
        "content" : "good",
        "score" : 5,
        "thumbsUpCount" : 0,
        "reviewCreatedVersion" : "22.9.3",
        "at" : "2022-01-17 10:48:11",
        "replyContent" : "-",
        "repliedAt" : "-"
}


### 3rd query ###

db.tik_tok.aggregate([{$project: {score: 1, date: { $substr: ["$at", 0, 10]}}}, {"$group": {_id: "$date", score:{$avg: "$score"}}}])

#### Output: ####

{ "_id" : "2022-02-28", "score" : 4.2766515621273555 }
{ "_id" : "2022-03-01", "score" : 4.342850818946436 }
{ "_id" : "2022-02-24", "score" : 4.343116883116883 }
{ "_id" : "2022-03-22", "score" : 4.355066771406127 }
{ "_id" : "2022-03-17", "score" : 4.294638694638695 }
{ "_id" : "2022-03-05", "score" : 4.308592835401545 }
{ "_id" : "2022-01-30", "score" : 4.320466321243523 }
{ "_id" : "2022-03-04", "score" : 4.349529003470501 }
{ "_id" : "2022-03-14", "score" : 4.289981972701519 }
{ "_id" : "2022-01-22", "score" : 4.337181337181337 }
{ "_id" : "2022-03-23", "score" : 4.297648211660951 }
{ "_id" : "2022-03-31", "score" : 4.318956611570248 }
{ "_id" : "2022-02-10", "score" : 4.2653118825853795 }
{ "_id" : "2022-01-28", "score" : 4.355549358616844 }
{ "_id" : "2022-01-25", "score" : 4.305135951661631 }
{ "_id" : "2022-03-26", "score" : 4.3132730732635585 }
{ "_id" : "2022-02-26", "score" : 4.298309178743962 }
{ "_id" : "2022-03-13", "score" : 4.31335952848723 }
{ "_id" : "2022-01-29", "score" : 4.309254498714653 }
{ "_id" : "2022-03-08", "score" : 4.306001481847369 }
