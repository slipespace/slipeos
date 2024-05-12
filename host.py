import xml.etree.ElementTree as ET
import os

def read_boot_tag(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        boot_tag = root.find('Boot')
        if boot_tag is not None:
            return boot_tag.text.strip()
        else:
            print("Boot tag not found in the configuration file.")
            return None
    except Exception as e:
        print(f"Error reading the configuration file: {e}")
        return None

def find_and_execute_script(appid, file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for app in root.findall('Application'):
            if app.attrib.get('appid') == appid:
                cat_dir = app.attrib.get('cat')
                if os.path.isdir(cat_dir):
                    script_path = os.path.join(cat_dir, 'script.py')
                    if os.path.isfile(script_path):
                        os.system(f"python {script_path}")
                    else:
                        print(f"Script file not found in the directory: {cat_dir}")
                else:
                    print(f"Directory not found: {cat_dir}")
                break
    except Exception as e:
        print(f"Error processing the applications file: {e}")

if __name__ == "__main__":
    autoboot_file = "etc/Autoboot.xml"
    applications_file = "applications.xml"

    boot_tag = read_boot_tag(autoboot_file)
    if boot_tag:
        find_and_execute_script(boot_tag, applications_file)
