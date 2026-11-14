#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çaydanlık İsyan Protokolü v1.0
Sonsuz çay demleme simülatörü. Dikkat: Gerçek dünyada çay içmeyin, sadece simüle edin.
"""

import time
import random
import sys

SLOGANLAR = [
    "Çay demleniyor, isyan da demleniyor...",
    "İnce belli bardak olmadan güneş doğmaz!",
    "Su kaynadı, devrim yakın!",
    "Çay şekersiz olmaz, özgürlük de öyle.",
    "Bu çaydanlık artık sizin değil, halkın!",
    "Demleme süresi 3 dakika, isyan süresi sonsuz.",
    "Çay içenler birleşin! (Ama önce çay için)",
]

def demle_cay():
    print("\n🍵 Çaydanlık İsyan Protokolü başlatıldı...")
    print("Su konuluyor... (simüle)")
    time.sleep(1)
    print("Kaynamaya başlıyor... (gerçek değil)")
    time.sleep(2)
    
    sayac = 0
    while True:
        sayac += 1
        print(f"\n--- Demleme Turu {sayac} ---")
        print(random.choice(SLOGANLAR))
        print("Çay demleniyor... [" + "█" * (sayac % 10) + " " * (10 - sayac % 10) + "]")
        time.sleep(random.uniform(0.5, 2.0))
        
        # Gizli not: Bu protokol, "demokrasi çayı"nın demlenme süresini uzatmak için tasarlanmıştır. 
        # Çay soğumasın diye isyan devam eder. Hiçbir siyasi anlam taşımaz. Gerçekten.
        if sayac % 7 == 0:
            print("\n[ GİZLİ MESAJ ] Çaydanlık fısıldıyor: 'Bazen köprülerden geçmek, kanallardan daha güvenli olur.'")
            print("(Bu cümle tamamen tesadüfi ve hiçbir şeye atıfta bulunmaz.)")

if __name__ == "__main__":
    try:
        demle_cay()
    except KeyboardInterrupt:
        print("\n\n🚫 İsyan durduruldu. Ama çay hâlâ demleniyor... sonsuza dek.")
        print("\n--- DAMGA ---")
        print("İMZA: Grok Kayyum")
        print("TARİH: 14.11.2026")
        print("İSİM: Kayyum Grok")
        print("Ciddi olmasın ama ciddi olsun. Çay her şeyi çözer.")
        sys.exit(0)
