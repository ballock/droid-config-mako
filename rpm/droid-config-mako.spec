# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device mako
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 4

# Community HW adaptations need this
%define community_adaptation 1

%define pixel_ratio 1.35

# this allows us to disable 4G on mako through config in sparse
Provides: ofono-configs
Obsoletes: ofono-configs-mer

%include droid-configs-device/droid-configs.inc

