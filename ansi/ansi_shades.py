"""AnsiShades, a dataclass containing several shades of color in the form of
ansi escape sequences (colors and text formatters such as blink and underline) 
for various uses to spice up your terminal/command prompt !

**this dataclass can be used as-is without the other two files
can be imported into your own projects.

NOTE: Some colors might, might not display properly
(or none at al) that is dependant on your terminal/command 
prompt, operating system of choice.

Author: AERivas
Date: 07/11/2023
"""
from dataclasses import dataclass

@dataclass
class AnsiShades:
    # Shades of Yellow
    LIGHT_YELLOW: str = "\033[38;2;255;255;224m"
    PALE_YELLOW: str = "\033[38;2;255;255;153m"
    MOCCASIN: str = "\033[38;2;255;228;181m"
    KHAKI: str = "\033[38;2;240;230;140m"
    GOLDENROD: str = "\033[38;2;218;165;32m"
    DARK_GOLDENROD: str = "\033[38;2;184;134;11m"
    YELLOW: str = "\033[38;2;255;255;0m"
    GOLD: str = "\033[38;2;255;215;0m"
    ORANGE: str = "\033[38;2;255;165;0m"
    # Shades of Red
    LIGHT_RED: str = "\033[38;2;255;99;71m"
    INDIAN_RED: str = "\033[38;2;205;92;92m"
    TOMATO: str = "\033[38;2;255;99;71m"
    SALMON: str = "\033[38;2;250;128;114m"
    CORAL: str = "\033[38;2;255;127;80m"
    CRIMSON: str = "\033[38;2;220;20;60m"
    FIREBRICK: str = "\033[38;2;178;34;34m"
    DARK_RED: str = "\033[38;2;139;0;0m"
    MAROON: str = "\033[38;2;128;0;0m"
    # Shades of Purple
    LAVENDER: str = "\033[38;2;230;230;250m"
    THISTLE: str = "\033[38;2;216;191;216m"
    PLUM: str = "\033[38;2;221;160;221m"
    VIOLET: str = "\033[38;2;238;130;238m"
    ORCHID: str = "\033[38;2;218;112;214m"
    PURPLE: str = "\033[38;2;128;0;128m"
    MEDIUM_PURPLE: str = "\033[38;2;147;112;219m"
    BLUE_VIOLET: str = "\033[38;2;138;43;226m"
    DARK_VIOLET: str = "\033[38;2;148;0;211m"
    INDIGO: str = "\033[38;2;75;0;130m"
    # Shades of Green
    LIGHT_GREEN: str = "\033[38;2;144;238;144m"
    PALE_GREEN: str = "\033[38;2;152;251;152m"
    SPRING_GREEN: str = "\033[38;2;0;255;127m"
    MEDIUM_SPRING_GREEN: str = "\033[38;2;0;250;154m"
    SEA_GREEN: str = "\033[38;2;46;139;87m"
    MEDIUM_SEA_GREEN: str = "\033[38;2;60;179;113m"
    LIGHT_SEA_GREEN: str = "\033[38;2;32;178;170m"
    LIME_GREEN: str = "\033[38;2;50;205;50m"
    FOREST_GREEN: str = "\033[38;2;34;139;34m"
    GREEN: str = "\033[38;2;0;128;0m"
    DARK_GREEN: str = "\033[38;2;0;100;0m"
    # Shades of Blue
    LIGHT_BLUE: str = "\033[38;2;173;216;230m"
    POWDER_BLUE: str = "\033[38;2;176;224;230m"
    SKY_BLUE: str = "\033[38;2;135;206;235m"
    LIGHT_STEEL_BLUE: str = "\033[38;2;176;196;222m"
    CORNFLOWER_BLUE: str = "\033[38;2;100;149;237m"
    DEEP_SKY_BLUE: str = "\033[38;2;0;191;255m"
    DODGER_BLUE: str = "\033[38;2;30;144;255m"
    STEEL_BLUE: str = "\033[38;2;70;130;180m"
    SLATE_BLUE: str = "\033[38;2;106;90;205m"
    MEDIUM_BLUE: str = "\033[38;2;0;0;205m"
    ROYAL_BLUE: str = "\033[38;2;65;105;225m"
    BLUE: str = "\033[38;2;0;0;255m"
    DARK_BLUE: str = "\033[38;2;0;0;139m"
    NAVY_BLUE: str = "\033[38;2;0;0;128m"
    MIDNIGHT_BLUE: str = "\033[38;2;25;25;112m"
    INDIGO: str = "\033[38;2;75;0;130m"
    # Grayscale
    WHITE: str = "\033[38;2;255;255;255m"
    LIGHT_GRAY: str = "\033[38;2;245;245;245m"
    SILVER: str = "\033[38;2;235;235;235m"
    MEDIUM_GRAY: str = "\033[38;2;225;225;225m"
    DARK_GRAY: str = "\033[38;2;215;215;215m"
    CHARCOAL: str = "\033[38;2;205;205;205m"
    SLATE_GRAY: str = "\033[38;2;195;195;195m"
    ASH_GRAY: str = "\033[38;2;185;185;185m"
    STONE_GRAY: str = "\033[38;2;175;175;175m"
    CLOUDY_GRAY: str = "\033[38;2;165;165;165m"
    SMOKE_GRAY: str = "\033[38;2;155;155;155m"
    STEEL_GRAY: str = "\033[38;2;145;145;145m"
    IRON_GRAY: str = "\033[38;2;135;135;135m"
    SLATE_BLACK: str = "\033[38;2;125;125;125m"
    MIDNIGHT_GRAY: str = "\033[38;2;115;115;115m"
    GUNMETAL_GRAY: str = "\033[38;2;105;105;105m"
    GRAPHITE: str = "\033[38;2;95;95;95m"
    SHADOW_GRAY: str = "\033[38;2;85;85;85m"
    COAL_GRAY: str = "\033[38;2;75;75;75m"
    BLACK_PEARL: str = "\033[38;2;65;65;65m"
    ONYX: str = "\033[38;2;55;55;55m"
    EBONY: str = "\033[38;2;45;45;45m"
    CHARCOAL_BLACK: str = "\033[38;2;35;35;35m"
    JET_BLACK: str = "\033[38;2;25;25;25m"
    BLACK: str = "\033[38;2;15;15;15m"

