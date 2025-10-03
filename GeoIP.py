#setup: pip install geoip2
#Get DB file from GeoLite2-City DB
import geoip2.database

DB_PATH = r"C:\Users\shraddha_mhatre\Documents\Plugins\GeoIP\GeoLite2-City.mmdb"

def print_record_geoip2(tgt):
    try:
        with geoip2.database.Reader(DB_PATH) as reader:
            resp = reader.city(tgt)
            city = resp.city.name or 'N/A'
            region = resp.subdivisions.most_specific.name or 'N/A'
            country = resp.country.name or 'N/A'
            lat = resp.location.latitude
            lon = resp.location.longitude

            print(f"[*] Target: {tgt} - Geo-located.")
            print(f"[+] {city}, {region}, {country}")
            print(f"[+] Latitude: {lat}, Longitude: {lon}")
    except geoip2.errors.AddressNotFoundError:
        print(f"[-] No geo record found for {tgt}")
    except Exception as e:
        print(f"[!] Error looking up {tgt}: {e}")

if __name__ == "__main__":
    print_record_geoip2('173.255.226.98')