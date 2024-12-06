from data_pipeline import DataPipeline
from model_development import ModelDevelopment
from security import Security
from api import ModelAPI, app
from monitoring import Monitoring
from kubernetes import deploy_kubernetes

# --------------------
# Ana Akış
# --------------------
if __name__ == "__main__":
    # Veri İşleme
    data_pipeline = DataPipeline("data.csv")
    raw_data = data_pipeline.load_data()
    clean_data = data_pipeline.clean_data(raw_data)
    X_train, X_test, y_train, y_test = data_pipeline.split_data(clean_data, target_column="target")

    # Model Geliştirme
    model_dev = ModelDevelopment(input_shape=X_train.shape[1])
    model = model_dev.build_model()
    trained_model = model_dev.train_model(model, X_train, y_train)

    # Tahmin ve Doğruluk
    y_pred = trained_model.predict(X_test).round()
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Güvenlik Örneği
    security = Security()
    key = security.generate_key()
    encrypted = security.encrypt_data("Gizli Veri", key)
    decrypted = security.decrypt_data(encrypted, key)
    print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")

    # API Çalıştırma
    model_api = ModelAPI(trained_model)
    app.run(debug=True)

    # Kubernetes Dağıtımı
    deploy_kubernetes()

    # İzleme
    Monitoring.setup_logging()
    Monitoring.log_message("Başlangıç işlemi tamamlandı.")
