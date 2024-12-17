import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sayfa başlığı
st.title("AICS - AI Tabanlı Kripto Dashboard")

# Coin Fiyatları - CoinGecko API'den veri çekme
st.subheader("📊 En Büyük 5 Coin Fiyatları")
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    'ids': 'bitcoin,ethereum,binancecoin,solana,cardano',
    'vs_currencies': 'usd',
    'include_24hr_change': 'true'
}
try:
    response = requests.get(url, params=params)
    data = response.json()

    # Fiyat ve değişimleri gösterme
    for coin, details in data.items():
        st.write(f"**{coin.capitalize()}**: ${details['usd']}  (24h: {details['usd_24h_change']:.2f}%)")
except Exception as e:
    st.error(f"API'den veri çekme hatası: {e}")

# AI Destekli Fiyat Tahminleri
st.subheader("🤖 AI Destekli Fiyat Tahminleri")

# Rastgele tahmin verisi oluşturma (örnek)
hours = np.arange(48)
btc_prices = 50000 + np.cumsum(np.random.randn(48))  # BTC tahmini
eth_prices = 3400 + np.cumsum(np.random.randn(48))   # ETH tahmini

# BTC Tahmini Grafiği
fig, ax = plt.subplots()
ax.plot(hours, btc_prices, label="BTC Tahmini", color="blue")
ax.plot(hours, eth_prices, label="ETH Tahmini", color="green")
ax.set_title("48 Saatlik Fiyat Tahminleri")
ax.set_xlabel("Saat")
ax.set_ylabel("Fiyat (USD)")
ax.legend()
st.pyplot(fig)

# Son 5 Kripto Haberi (Örnek Haberler)
st.subheader("📰 Son 5 Kripto Haberi")
news = [
    "1. Bitcoin yeniden $50K seviyesini geçti.",
    "2. Ethereum yükselen trendde teknik sinyal verdi.",
    "3. Solana ekosisteminde yeni NFT patlaması yaşanıyor.",
    "4. Binance yeni launchpad duyurusunu yaptı.",
    "5. Kripto piyasasında günlük hacim %20 arttı."
]
for item in news:
    st.write(item)
