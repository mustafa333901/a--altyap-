from textblob import TextBlob

# --------------------
# 8. Trend ve Geri Bildirim Analizi
# --------------------
class TrendAnalysis:
    def __init__(self, social_media_data):
        self.social_media_data = social_media_data

    def analyze_trends(self):
        """Sosyal medya verilerinde trend analizi yapar."""
        trend_words = []
        for data in self.social_media_data:
            sentiment_score = TextBlob(data['text']).sentiment.polarity
            if sentiment_score > 0.1:  # Pozitif duygu içeren metinler
                trend_words.append(data['text'])
        return trend_words

class UserFeedback:
    def __init__(self):
        self.feedback_data = []

    def collect_feedback(self, user_id, feedback):
        """Kullanıcı geri bildirimi toplar."""
        self.feedback_data.append({
            "user_id": user_id,
            "feedback": feedback
        })

    def analyze_feedback(self):
        """Geri bildirimleri analiz eder."""
        feedback_sentiments = []
        for feedback in self.feedback_data:
            sentiment = TextBlob(feedback['feedback']).sentiment.polarity
            feedback_sentiments.append(sentiment)
        return feedback_sentiments
