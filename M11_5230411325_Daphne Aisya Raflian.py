import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsRegressor  # Ganti ke KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

class QualityAir:
    def init(self, data):
        self.data = data
        
        # Memeriksa dan menangani nilai NaN
        if self.data.isnull().values.any():
            print("Data mengandung nilai NaN. Menghapus baris dengan nilai NaN.")
            self.data = self.data.dropna()  # Menghapus baris dengan nilai NaN
        
        if 'Air Quality' not in self.data.columns:
            raise ValueError("Kolom 'Air Quality' tidak ditemukan dalam data.")
        
        # Mengonversi nilai Air Quality yang berupa string ke angka
        label_encoder = LabelEncoder()
        self.data['Air Quality'] = label_encoder.fit_transform(self.data['Air Quality'])
        
        # Memeriksa hasil konversi
        print("Data setelah konversi 'Air Quality' ke angka:")
        print(self.data['Air Quality'].unique())  # Menampilkan nilai unik setelah konversi
        
        self.X = self.data.drop(['Air Quality'], axis=1)
        self.y = self.data['Air Quality']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.train_model()  


    
    @staticmethod
    def Membaca_xlsx(air_quality.xlsx):
        try:
            data = pd.read_excel(air_quality.xlsx)  # Menggunakan parameter file_path yang diterima
            return data
        except FileNotFoundError:
            print(f"File '{air_quality.xlsx}' tidak ditemukan. Pastikan path dan nama file sudah benar.")
            return None
    
    def train_model(self):
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, self.y_pred)
        self.classification_report = classification_report(self.y_test, self.y_pred)
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)
        self.feature_importances = self.model.feature_importances_
        self.feature_names = self.X.columns
        self.feature_importances_df = pd.DataFrame({'feature': self.feature_names, 'importance': self.feature_importances})
        self.plot_importances()
        self.plot_confusion_matrix()
    
    def plot_importances(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(x="feature", y="importance", data=self.feature_importances_df)
        plt.title("Feature Importances")
        plt.xlabel("Feature")
        plt.ylabel("Importance")
        plt.show()
    
    def plot_confusion_matrix(self):
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.confusion_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.show()

class Regresi:
    def init(self, data):
        self.data = data
        if 'Air Quality' not in data.columns:
            raise ValueError("Kolom 'Air Quality' tidak ditemukan.")
        
        # Mengonversi Air Quality ke angka seperti yang dilakukan di kelas QualityAir
        label_encoder = LabelEncoder()
        self.data['Air Quality'] = label_encoder.fit_transform(self.data['Air Quality'])
        
        # Menggunakan data kontinu untuk regresi
        self.X = data.drop(['Air Quality'], axis=1)
        self.y = data['Air Quality']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def Regresi_Linier(self):
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        print("Mean Squared Error Regresi Linier:", mse)

    def Regresi_Vektor_Pendukung_SVR(self):
        model = SVR()
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        print("Mean Squared Error SVR:", mse)

    def Regresi_KNN(self):  # Menambahkan metode regresi KNN
        model = KNeighborsRegressor(n_neighbors=5)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        print("Mean Squared Error KNN:", mse)



# Menu interaksi pengguna
while True:
    print("1. Membaca XLSX")
    print("2. Training Model")
    print("3. Regresi ada 3 menu")
    print("4. Exit")
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        file_name = input("Masukkan nama file XLSX (misal: data.xlsx): ")
        data = QualityAir.Membaca_xlsx(file_name)  
        if data is not None:
            try:
                quality_air = QualityAir(data)  
                print("Data berhasil dimuat.")
                print("\nBeberapa baris pertama dari data:")
                print(quality_air.data.head())  
            except ValueError as e:
                print(e)
        
    elif pilihan == "2":
        if 'quality_air' in locals(): 
            quality_air.train_model() 
            print("Model telah dilatih.")
            print("Akurasi:", quality_air.accuracy)
            print("Laporan Klasifikasi:\n", quality_air.classification_report)
        else:
            print("Silakan muat data terlebih dahulu.")
    
    elif pilihan == "3":
        if 'quality_air' in locals():
            regresi = Regresi(quality_air.data)
            print("Pilih metode regresi:")
            print("1. Regresi Linier")
            print("2. (SVR)")
            print("3.(KNN)")
            regresi_pilihan = input("Pilih metode: ")
            if regresi_pilihan == "1":
                regresi.Regresi_Linier()
            elif regresi_pilihan == "2":
                regresi.Regresi_Vektor_Pendukung_SVR()
            elif regresi_pilihan == "3":
                regresi.Regresi_KNN()
            else:
                print("Pilihan tidak valid.")
        else:
            print("Silakan muat data terlebih dahulu.")
    
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid")
