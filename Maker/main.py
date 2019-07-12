# due to my level, i cant find the english font.
import StreamHelper, string, csv;
from StringHelper import StringHelper;
from UnityFont import UnityFont;

def gen_csv():
	key_arr = [];
	value_arr = [];

	f = open('OriginalFile/unnamed asset-resources.assets-261.dat', 'rb');
	gameobj_fielID = StreamHelper.read_int32(f);
	gameobj_pathID = StreamHelper.read_int64(f);
	gameobj_enabled = StreamHelper.read_uint32(f);
	script_fielID = StreamHelper.read_int32(f);
	script_pathID = StreamHelper.read_int64(f);
	script_name = StreamHelper.read_aligned_string(f);
	
	len = StreamHelper.read_int32(f);
	for i in range(len):
		key_arr.append(StreamHelper.read_aligned_string(f));
		value_arr.append(StreamHelper.read_aligned_string(f));

	f.close();

	f = open('localization.csv', 'wb');
	csv_writer = csv.writer(f);
	
	for i in range(len):
		csv_writer.writerow([value_arr[i], "", key_arr[i]]);

	f.close();

def csv_to_raw():
	key_arr = [];
	value_arr = [];
	
	f = open('OriginalFile/unnamed asset-resources.assets-266.dat', 'rb');
	gameobj_fielID = StreamHelper.read_int32(f);
	gameobj_pathID = StreamHelper.read_int64(f);
	gameobj_enabled = StreamHelper.read_uint32(f);
	script_fielID = StreamHelper.read_int32(f);
	script_pathID = StreamHelper.read_int64(f);
	script_name = StreamHelper.read_aligned_string(f);
	f.close();
	
	f = open('localization.new.csv', 'rb');
	csv_reader = csv.reader(f);
	
	for row in csv_reader:
		key_arr.append(row[2]);
		value_arr.append(row[1]);
	
	f.close();
	
	f = open('Broforce/unnamed asset-resources.assets-266.dat', 'wb');

	gameobj_fielID = StreamHelper.write_int32(f, gameobj_fielID);
	gameobj_pathID = StreamHelper.write_int64(f, gameobj_pathID);
	gameobj_enabled = StreamHelper.write_uint32(f, gameobj_enabled);
	script_fielID = StreamHelper.write_int32(f, script_fielID);
	script_pathID = StreamHelper.write_int64(f, script_pathID);
	script_name = StreamHelper.write_aligned_string(f, script_name);
	
	StreamHelper.write_int32(f, len(key_arr));
	for i in range(len(key_arr)):
		StreamHelper.write_aligned_string(f, key_arr[i]);
		StreamHelper.write_aligned_string(f, value_arr[i]);
	
	f.close();
	
	
def gen_unity_font():
	sh = StringHelper();
	sh.code = "dos";
	sh.add_file_text("localization.new.csv");
	sh.add_western();

	font = UnityFont("OriginalFile/unnamed asset-sharedassets0.assets-24.dat", unity_version = [2017, 4, 1, 0], version = 17);
	font.character_spacing = 2;
	font.convert_to_raw("Broforce/unnamed asset-sharedassets0.assets-24.dat", "C:/Windows/Fonts/SourceHanSansSC-Bold.otf");
	
csv_to_raw();
gen_unity_font();
