# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from pyecharts import GeoLines, Style
import pyecharts


style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    symbol = 'circle',
    symbol_size  = 1.5,
    legend_selectedmode="multiple",
)


def test_geolines():
    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]
    data_beijing = [
        ["北京", "上海"],
        ["北京", "广州"],
        ["北京", "南京"],
        ["北京", "重庆"],
        ["北京", "兰州"],
        ["北京", "杭州"]
    ]
    '''
    data_all = [
        ["北京", "上海"],
        ["北京", "广州"],
        ["北京", "南京"],
        ["北京", "重庆"],
        ["北京", "兰州"],
        ["北京", "杭州"],
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]       
        ]
        '''
    lines = GeoLines("GeoLines 示例", **style.init_style)
    lines.add("从广州出发", data_guangzhou, **style_geo)
    lines.add("从北京出发", data_beijing, **style_geo)
    #lines.add("ALL", data_all, **style_geo)
    lines.show_config()
    lines.render('geolines.html')
#    lines.add(angle_data, angle_range, area_color, area_opacity, axis_range, bar_category_gap, border_color, boundary_gap, center, calendar_date_range, calendar_cell_size, datazoom_type, datazoom_range, datazoom_orient, datazoom_xaxis_index, datazoom_yaxis_index, effect_brushtype, effect_period, effect_scale, extra_data, geo_emphasis_color, geo_normal_color, geo_cities_coords, geo_effect_period, geo_effect_traillength, geo_effect_color, geo_effect_symbol, geo_effect_symbolsize, graph_layout, graph_gravity, graph_edge_length, graph_repulsion, graph_edge_symbol, graph_edge_symbolsize, grid_width, grid_height, grid_top, grid_bottom, grid_left, grid_right, grid3d_width, grid3d_height, grid3d_depth, grid3d_opacity, grid3d_shading, grid3d_rotate_speed, grid3d_rotate_sensitivity, is_angleaxis_show, is_area_show, is_axisline_show, is_calculable, is_calendar_heatmap, is_clockwise, is_convert, is_datazoom_show, is_fill, is_focusnode, is_geo_effect_show, is_grid3d_rotate, is_label_show, is_label_emphasis, is_legend_show, is_liquid_animation, is_liquid_outline_show, is_more_utils, is_piecewise, is_radiusaxis_show, is_random, is_roam, is_rotatelabel, is_smooth, is_splitline_show, is_stack, is_step, is_symbol_show, is_map_symbol_show, is_visualmap, is_xaxislabel_align, is_yaxislabel_align, is_xaxis_inverse, is_yaxis_inverse, is_xaxis_boundarygap, is_yaxis_boundarygap, is_xaxis_show, is_yaxis_show, item_color, label_color, label_pos, label_text_color, label_text_size, label_formatter, label_emphasis_textcolor, label_emphasis_textsize, label_emphasis_pos, legend_orient, legend_pos, legend_top, legend_selectedmode, legend_text_size, legend_text_color, line_curve, line_opacity, line_type, line_width, line_color, liquid_color, maptype, mark_line, mark_line_symbolsize, mark_line_valuedim, mark_point, mark_point_symbol, mark_point_symbolsize, mark_point_textcolor, radius_data, radius, rosetype, rotate_step, scale_range, shape, start_angle, symbol_size, symbol, sankey_node_width, sankey_node_gap, type, tooltip_tragger, tooltip_tragger_on, tooltip_axispointer_type, tooltip_formatter, tooltip_text_color, tooltip_font_size, treemap_left_depth, treemap_drilldown_icon, treemap_visible_min, visual_orient, visual_range_color, visual_range_size, visual_range_text, visual_range, visual_text_color, visual_pos, visual_top, visual_type, visual_split_number, visual_dimension, word_gap, word_size_range, x_axis, xaxis_margin, xaxis_interval, xaxis_force_interval, xaxis_pos, xaxis_name_gap, xaxis_name_size, xaxis_name_pos, xaxis_name, xaxis_rotate, xaxis_min, xaxis_max, xaxis_type, xaxis3d_name, xaxis3d_name_size, xaxis3d_name_gap, xaxis3d_min, xaxis3d_max, xaxis3d_interval, xaxis3d_margin, yaxis_margin, yaxis_interval, yaxis_force_interval, yaxis_pos, yaxis_formatter, yaxis_rotate, yaxis_min, yaxis_max, yaxis_name_gap, yaxis_name_size, yaxis_name_pos, yaxis_type, yaxis_name, yaxis3d_name, yaxis3d_name_size, yaxis3d_name_gap, yaxis3d_min, yaxis3d_max, yaxis3d_interval, yaxis3d_margin, zaxis3d_name, zaxis3d_name_size, zaxis3d_name_gap, zaxis3d_min, zaxis3d_max, zaxis3d_margin)
test_geolines()
print 'ok'