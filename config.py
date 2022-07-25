# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"
        ),
    Key([mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"
        ),
    Key([mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
        ),
    Key([mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
        ),
    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
        ),
    Key([mod, "control"], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
        ),
    Key([mod, "control"], "k", 
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),
    Key(
        [mod], "b",
        lazy.spawn('brave'),
        desc="Launch firefox"
    ),
    Key(
        [mod], "m",
        lazy.spawn('alacritty -e cmus'),
        desc="Launch cmus music player"
    ),
    Key(
        [mod], "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc="Launch emacs"
    ),
    Key([], "Print", lazy.spawn("scrot '~/pic/ss/ss_%Y-%m-%d.jpg'")),
    Key(
        [mod], "p",
        lazy.spawn("scrot '/home/lithium/pic/ss/ss.jpg'"),
        desc="Takes screenshot"
    ),
    Key(
        [mod, "shift"], "p",
        lazy.spawn("scrot -scapture '/home/lithium/pic/ss/ss.jpg'"),
        desc="Takes screenshot"
    ),
    Key(
        [mod], "d",
        lazy.spawn("discord"),
        desc="Launch discord"
    ),
    Key(
        [], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +10%")
    ),
    Key(
        [], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5")
    ),
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5")
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key(
        [mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key(
        [mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
    ),
    Key(
        [mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),
    Key(
        [mod], "r",
        lazy.spawn("dmenu_run"),
        desc="Start dmenu"
    ),
]

group_names = [("", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),
    ("ﭮ", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),
    ("", {'layout': 'columns'}),]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layouts = [
    layout.Columns(
        border_focus="#44475a",
        border_focus_stack=["#44475a", "#8f3d3d"],
        border_normal="#282a36",
        border_normal_stack="#8f3d3d",
        border_width=2,
        border_on_single=True,
        margin=6,
        fair=True,
        grow_amount=5,
    ),
    layout.Max(),
    layout.Floating(
        border_normal="#6272A4",
        border_focus="#44475A",
        border_width=2
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(
        border_focus="#44475a",
        border_normal="#282a36",
        border_width=2,
        columns=2,
        margin=2
    ),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    background='21222C',
    foreground='F8F8F2',
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    padding=5,
                    rounded=False,
                    highlight_method='block',
                    background='BD93F9',
                    inactive='4c566a',
                    urgent_text='FF5555',
                    active='434c5e',
                    this_current_screen_border='D6ACFF'
                ),
                widget.Spacer(
                    length=8,
                    background='BD93F9',
                ),
                # widget.TextBox(
                #     " ",
                #     foreground='BD93F9',
                #     fontsize=19,
                #     padding=0
                # ),
                widget.Spacer(
                    length=5,
                ),
                widget.WindowName(
                    font='JetBrains Mono',
                ),
                widget.Systray(
                    icon_size=15,
                    padding=10,
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.CPU(
                    background='#44475a',
                    format=' {load_percent}%',
                    padding=8
                ),
                widget.Memory(
                    background='#6272a4',
                    format='{MemUsed: .0f}{mm}',
                    measure_mem='M',
                    update_interval=1.0,
                    padding=8
                ),
                widget.Clock(
                    background='#50FA7B',
                    foreground='#282A36',
                    format="%a %b %x %I:%M %p",
                    padding=5,
                ),
                widget.Spacer(
                    length=5,
                ),
                widget.Volume(
                    background='#8be9fd',
                    foreground='#44475a',
                    fmt='墳 {}',
                    volume_down_command='pamixer -d 5',
                    volume_up_command='pamixer -i 5',
                    volume_app='pavumixer',
                    step=1,
                    padding=7
                ),
                # widget.TextBox(
                #     '',
                #     foreground='FFB86C',
                #     fontsize=19,
                #     padding=0
                # ),
                widget.Backlight(
                    # background=None,
                    fmt=' {}',
                    backlight_name='radeon_bl0',
                    brightness_file='brightness',
                    max_brightness_file='max_brightness',
                    padding=10
                    # change_command='brightnessctl set '
                ),
                widget.Battery(
                    battery=1,
                    charge_char='  ',
                    discharge_char='  ',
                    empty_char='  ',
                    full_char='  ',
                    format='{char}{percent:2.0%}',
                    low_foreground='FF5555',
                    low_percentage=0.25,
                    show_short_text=False,
                    update_interval=120,
                    padding=5
                ),
                widget.QuickExit(
                    font='JetBrainsMono Nerd Font',
                    fontsize='17',
                    background='FFB86C',
                    foreground='FF5555',
                    default_text='襤',
                    padding=8,
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
