import qrcode

wifi_type = "WPA"
wifi_ssid = "aus14_2"
wifi_password = "#41AUSUA14#"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
# img = qrcode.make(wifi)
# type(img)  # qrcode.image.pil.PilImage
qrcode.make(wifi).save("SUA.png")