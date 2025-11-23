reset = '\033[0m'
red = '\033[31m'
wvw_color = "\u001b[38;2;111;252;245m"
it_color = "\u001b[38;2;178;178;178m"
wbw_color = "\u001b[38;2;156;97;20m"
gg_color = "\u001b[38;2;219;181;9m"

sr_color = "\u001b[38;2;231;237;38m"
rr_color = "\u001b[38;2;232;16;124m"
cs_color = "\u001b[38;2;219;128;9m"

ff_color = "\u001b[38;2;185;227;235m"
bcg_color = "\u001b[38;2;183;0;255m"
sfs_color = "\u001b[38;2;170;91;201m"

og_color = "\u001b[38;2;31;181;33m"
sl_color = "\u001b[38;2;9;230;218m"
sls_color = "\u001b[38;2;145;191;189m"

ci_color = "\u001b[38;2;220;150;4m"
aa_color = "\u001b[38;2;45;109;247m"
mm_color = "\u001b[38;2;116;54;255m"

ac_color = "\u001b[38;2;45;149;252m"
ab_color = "\u001b[38;2;220;115;4m"
ec_color = "\u001b[38;2;219;40;4m"
srs_color = "\u001b[38;2;150;150;150m"

default_color = "\u001b[38;2;255;255;255m"
white = "\u001b[38;2;255;255;255m"
light_red = "\u001b[38;2;255;0;0m"
red = "\u001b[38;2;128;0;0m"
dark_red = "\u001b[38;2;64;0;0m"
green = "\u001b[38;2;0;128;0m"
dark_green = "\u001b[38;2;0;64;0m"
light_blue = "\u001b[38;2;0;191;255m"
blue = "\u001b[38;2;0;128;255m"
dark_blue = "\u001b[38;2;0;64;128m"
orange = "\u001b[38;2;255;165;0m"
yellow = "\u001b[38;2;255;255;0m"
black = "\u001b[38;2;0;0;0m"

def get_color(name: str):
    if name == "Midnight Black":
        return srs_color
    if name == "Mysterious Purple":
        return mm_color
    if name == "Sky Blue":
        return aa_color
    if name == "Coal Black":
        return ci_color
    if name == "Teal":
        return ac_color
    if name == "Amber Orange":
        return ab_color
    if name == "Arctic Blue":
        return wvw_color
    if name == "Steel Gray":
        return it_color
    if name == "Brown":
        return wbw_color
    if name == "Royal Gold":
        return gg_color
    if name == "Radiant Yellow":
        return sr_color
    if name == "Crimson Red":
        return rr_color
    if name == "Rich Chesnut":
        return cs_color
    if name == "Misty Gray":
        return ff_color
    if name == "Onyx Black":
        return bcg_color
    if name == "Venomous Purple":
        return sfs_color
    if name == "Deep Green":
        return og_color
    if name == "Electric Blue":
        return sl_color
    if name == "Silver Metallic":
        return sls_color
    if name == "Ember Red":
        return ec_color
    return default_color