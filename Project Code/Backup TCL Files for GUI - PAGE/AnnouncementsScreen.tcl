#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  May 30, 2025 08:16:40 AM EEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) white
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
set vTcl(project_theme) default



proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #d9d9d9 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 600x450+341+136
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Toplevel 0"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "AnnouncementsScreen" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    frame "$top.fra47" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 425 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 565 
    vTcl:DefineAlias "$top.fra47" "announcementlabel" vTcl:WidgetProc "AnnouncementsScreen" 1
    set site_3_0 $top.fra47
    label "$site_3_0.lab48" \
        -activebackground #d9d9d9 -activeforeground black -anchor s \
        -background #ffffff -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 11 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "Announcement" 
    vTcl:DefineAlias "$site_3_0.lab48" "announcementtitle" vTcl:WidgetProc "AnnouncementsScreen" 1
    label "$site_3_0.lab55" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #0000ff -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #ffffff \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "TO DATE" 
    vTcl:DefineAlias "$site_3_0.lab55" "todate" vTcl:WidgetProc "AnnouncementsScreen" 1
    label "$site_3_0.lab54" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #0000ff -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #ffffff \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -text "FROM DATE" 
    vTcl:DefineAlias "$site_3_0.lab54" "fromdate" vTcl:WidgetProc "AnnouncementsScreen" 1
    checkbutton "$site_3_0.che53" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "HOSPITALITY" -variable "che53" 
    vTcl:DefineAlias "$site_3_0.che53" "hospitality" vTcl:WidgetProc "AnnouncementsScreen" 1
    checkbutton "$site_3_0.che52" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "ADOPTION" -variable "che52" 
    vTcl:DefineAlias "$site_3_0.che52" "adoption" vTcl:WidgetProc "AnnouncementsScreen" 1
    checkbutton "$site_3_0.che51" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "CAT" -variable "che51" 
    vTcl:DefineAlias "$site_3_0.che51" "cat" vTcl:WidgetProc "AnnouncementsScreen" 1
    button "$site_3_0.but57" \
        -activebackground #d9d9d9 -activeforeground black -background #0000ff \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #ffffff -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -text "SEARCH" 
    vTcl:DefineAlias "$site_3_0.but57" "SearchButton" vTcl:WidgetProc "AnnouncementsScreen" 1
    label "$site_3_0.lab49" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #0000ff -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9 -weight bold" -foreground #ffffff \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "SELECT" 
    vTcl:DefineAlias "$site_3_0.lab49" "selectlabel" vTcl:WidgetProc "AnnouncementsScreen" 1
    checkbutton "$site_3_0.che50" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -justify left \
        -text "DOG" -variable "che50" 
    vTcl:DefineAlias "$site_3_0.che50" "dog" vTcl:WidgetProc "AnnouncementsScreen" 1
    frame "$site_3_0.fra59" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 305 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 335 
    vTcl:DefineAlias "$site_3_0.fra59" "ResultFrame" vTcl:WidgetProc "AnnouncementsScreen" 1
    listbox "$site_3_0.lis56" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 -height 92 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 144 
    $site_3_0.lis56 configure -font "TkFixedFont"
    $site_3_0.lis56 insert end text
    vTcl:DefineAlias "$site_3_0.lis56" "ListDate" vTcl:WidgetProc "AnnouncementsScreen" 1
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.018 -y 0 -rely 0.024 -width 0 \
        -relwidth 0.945 -height 0 -relheight 0.073 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.518 -width 0 \
        -relwidth 0.166 -height 0 -relheight 0.049 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.447 -width 0 \
        -relwidth 0.149 -height 0 -relheight 0.049 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che53 \
        -in $site_3_0 -x 0 -relx 0.071 -y 0 -rely 0.353 -width 0 \
        -relwidth 0.179 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che52 \
        -in $site_3_0 -x 0 -relx 0.071 -y 0 -rely 0.306 -width 0 \
        -relwidth 0.161 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che51 \
        -in $site_3_0 -x 0 -relx 0.071 -y 0 -rely 0.259 -width 0 \
        -relwidth 0.108 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 0 -relx 0.106 -y 0 -rely 0.894 -width 57 -relwidth 0 \
        -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.035 -y 0 -rely 0.141 -width 0 \
        -relwidth 0.096 -height 0 -relheight 0.049 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che50 \
        -in $site_3_0 -x 0 -relx 0.071 -y 0 -rely 0.212 -width 0 \
        -relwidth 0.108 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra59 \
        -in $site_3_0 -x 0 -relx 0.354 -y 0 -rely 0.188 -width 0 \
        -relwidth 0.593 -height 0 -relheight 0.718 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lis56 \
        -in $site_3_0 -x 0 -relx 0.018 -y 0 -rely 0.612 -width 0 \
        -relwidth 0.255 -height 0 -relheight 0.216 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra47 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.022 -width 0 -relwidth 0.942 \
        -height 0 -relheight 0.944 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

