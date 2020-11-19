arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_model_stats.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: 1
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_100:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/DalyUncleared/ass_beststats.txt
    inputBinding:
      position: 100
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_101:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/DryRiver/ass_beststats.txt
    inputBinding:
      position: 101
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_102:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/SturtPlains/ass_beststats.txt
    inputBinding:
      position: 102
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_103:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/HowardSprings/ass_beststats.txt
    inputBinding:
      position: 103
      prefix: --lpjguess_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_104:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/AdelaideRiver/ass_beststats.txt
    inputBinding:
      position: 104
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_105:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/DalyUncleared/ass_beststats.txt
    inputBinding:
      position: 105
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_106:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/DryRiver/ass_beststats.txt
    inputBinding:
      position: 106
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_107:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/SturtPlains/ass_beststats.txt
    inputBinding:
      position: 107
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_108:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/HowardSprings/ass_beststats.txt
    inputBinding:
      position: 108
      prefix: --maespa_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_109:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/AdelaideRiver/ass_beststats.txt
    inputBinding:
      position: 109
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default: 1
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_110:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/DalyUncleared/ass_beststats.txt
    inputBinding:
      position: 110
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_111:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/DryRiver/ass_beststats.txt
    inputBinding:
      position: 111
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_112:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/SturtPlains/ass_beststats.txt
    inputBinding:
      position: 112
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_113:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/HowardSprings/ass_beststats.txt
    inputBinding:
      position: 113
      prefix: --spa_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_114:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/AdelaideRiver/ass_beststats.txt
    inputBinding:
      position: 114
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_115:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/DalyUncleared/ass_beststats.txt
    inputBinding:
      position: 115
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_116:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/DryRiver/ass_beststats.txt
    inputBinding:
      position: 116
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_117:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/SturtPlains/ass_beststats.txt
    inputBinding:
      position: 117
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_118:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/HowardSprings/ass_beststats.txt
    inputBinding:
      position: 118
      prefix: --cable_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_119:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/AdelaideRiver/ass_beststats.txt
    inputBinding:
      position: 119
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 12
      prefix: --dingo_et
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_120:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/DalyUncleared/ass_beststats.txt
    inputBinding:
      position: 120
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_121:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/DryRiver/ass_beststats.txt
    inputBinding:
      position: 121
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_122:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/SturtPlains/ass_beststats.txt
    inputBinding:
      position: 122
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_123:
    default: data/img/4_fitness.png
    inputBinding:
      position: 123
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default:
      class: File
      path: ../../data/DINGO/Ea_adelaide.txt
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/DINGO/Ea_sturt.txt
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 17
      prefix: --dingo_gpp
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_adelaide.txt
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default: Howard Springs
    inputBinding:
      position: 2
      prefix: --sites
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_20:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_sturt.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    inputBinding:
      position: 22
      prefix: --i2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 23
      prefix: --vom_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 28
      prefix: --vom_pc_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: Adelaide River
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_32:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/HowardSprings/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 33
      prefix: --vom_pc2_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/AdelaideRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DryRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/SturtPlains/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/HowardSprings/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 38
      prefix: --vom_zr_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_39:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/AdelaideRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: Daly River
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_40:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_41:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 41
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_42:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/SturtPlains/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_43:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/HowardSprings/evap_beststats.txt
    inputBinding:
      position: 43
      prefix: --bess_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_44:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/AdelaideRiver/evap_beststats.txt
    inputBinding:
      position: 44
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_45:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/DalyUncleared/evap_beststats.txt
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_46:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/DryRiver/evap_beststats.txt
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_47:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/SturtPlains/evap_beststats.txt
    inputBinding:
      position: 47
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_48:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/HowardSprings/evap_beststats.txt
    inputBinding:
      position: 48
      prefix: --bios2_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_49:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/AdelaideRiver/evap_beststats.txt
    inputBinding:
      position: 49
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default: Dry River
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_50:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/DalyUncleared/evap_beststats.txt
    inputBinding:
      position: 50
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_51:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/DryRiver/evap_beststats.txt
    inputBinding:
      position: 51
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_52:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/SturtPlains/evap_beststats.txt
    inputBinding:
      position: 52
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_53:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/HowardSprings/evap_beststats.txt
    inputBinding:
      position: 53
      prefix: --lpjguess_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_54:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/AdelaideRiver/evap_beststats.txt
    inputBinding:
      position: 54
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_55:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/DalyUncleared/evap_beststats.txt
    inputBinding:
      position: 55
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_56:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/DryRiver/evap_beststats.txt
    inputBinding:
      position: 56
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_57:
    default:
      class: File
      path: ../../data/SavMIP_stats/LPJGUESS/SturtPlains/evap_beststats.txt
    inputBinding:
      position: 57
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_58:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/HowardSprings/evap_beststats.txt
    inputBinding:
      position: 58
      prefix: --maespa_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_59:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/AdelaideRiver/evap_beststats.txt
    inputBinding:
      position: 59
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: Sturt Plains
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_60:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/DalyUncleared/evap_beststats.txt
    inputBinding:
      position: 60
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_61:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/DryRiver/evap_beststats.txt
    inputBinding:
      position: 61
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_62:
    default:
      class: File
      path: ../../data/SavMIP_stats/MAESPA/SturtPlains/evap_beststats.txt
    inputBinding:
      position: 62
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_63:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/HowardSprings/evap_beststats.txt
    inputBinding:
      position: 63
      prefix: --spa_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_64:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/AdelaideRiver/evap_beststats.txt
    inputBinding:
      position: 64
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_65:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/DalyUncleared/evap_beststats.txt
    inputBinding:
      position: 65
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_66:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/DryRiver/evap_beststats.txt
    inputBinding:
      position: 66
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_67:
    default:
      class: File
      path: ../../data/SavMIP_stats/SPA/SturtPlains/evap_beststats.txt
    inputBinding:
      position: 67
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_68:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/HowardSprings/evap_beststats.txt
    inputBinding:
      position: 68
      prefix: --cable_evap_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_69:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/AdelaideRiver/evap_beststats.txt
    inputBinding:
      position: 69
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: 1
    inputBinding:
      position: 7
      prefix: --whitley_sites
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_70:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/DalyUncleared/evap_beststats.txt
    inputBinding:
      position: 70
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_71:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/DryRiver/evap_beststats.txt
    inputBinding:
      position: 71
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_72:
    default:
      class: File
      path: ../../data/SavMIP_stats/CABLE/SturtPlains/evap_beststats.txt
    inputBinding:
      position: 72
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_73:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 73
      prefix: --vom_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_74:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 74
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_75:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 75
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_76:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 76
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_77:
    default:
      class: File
      path: ../../data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 77
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_78:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 78
      prefix: --vom_pc_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_79:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 79
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default: 1
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_80:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 80
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_81:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 81
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_82:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 82
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_83:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/HowardSprings/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 83
      prefix: --vom_pc2_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_84:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/AdelaideRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 84
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_85:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 85
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_86:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DryRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 86
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_87:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/SturtPlains/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 87
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_88:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/HowardSprings/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 88
      prefix: --vom_zr_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_89:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/AdelaideRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 89
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: 1
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_90:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 90
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_91:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 91
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_92:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/SturtPlains/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 92
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_93:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/HowardSprings/ass_beststats.txt
    inputBinding:
      position: 93
      prefix: --bess_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_94:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/AdelaideRiver/ass_beststats.txt
    inputBinding:
      position: 94
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_95:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/DalyUncleared/ass_beststats.txt
    inputBinding:
      position: 95
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_96:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/DryRiver/ass_beststats.txt
    inputBinding:
      position: 96
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_97:
    default:
      class: File
      path: ../../data/SavMIP_stats/BESS/SturtPlains/ass_beststats.txt
    inputBinding:
      position: 97
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_98:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/HowardSprings/ass_beststats.txt
    inputBinding:
      position: 98
      prefix: --bios2_gpp_stats
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_99:
    default:
      class: File
      path: ../../data/SavMIP_stats/BIOS2/AdelaideRiver/ass_beststats.txt
    inputBinding:
      position: 99
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_123)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_model_stats.py
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/DINGO/Ea_adelaide.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/DINGO/Ea_dry.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/DINGO/Ea_sturt.txt
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/DINGO/GPPdaily_adelaide.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/DINGO/GPPdaily_dry.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/DINGO/GPPdaily_sturt.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_29)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_30)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_31)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_32)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_33)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/HowardSprings/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_34)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/AdelaideRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_35)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_36)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DryRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_37)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/SturtPlains/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_38)
    entryname: data/VOM_output/additional_analyses/fixed_roots/HowardSprings/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_39)
    entryname: data/VOM_output/additional_analyses/fixed_roots/AdelaideRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_40)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_41)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_42)
    entryname: data/VOM_output/additional_analyses/fixed_roots/SturtPlains/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_43)
    entryname: data/SavMIP_stats/BESS/HowardSprings/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_44)
    entryname: data/SavMIP_stats/BESS/AdelaideRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_45)
    entryname: data/SavMIP_stats/BESS/DalyUncleared/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_46)
    entryname: data/SavMIP_stats/BESS/DryRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_47)
    entryname: data/SavMIP_stats/BESS/SturtPlains/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_48)
    entryname: data/SavMIP_stats/BIOS2/HowardSprings/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_49)
    entryname: data/SavMIP_stats/BIOS2/AdelaideRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_50)
    entryname: data/SavMIP_stats/BIOS2/DalyUncleared/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_51)
    entryname: data/SavMIP_stats/BIOS2/DryRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_52)
    entryname: data/SavMIP_stats/BIOS2/SturtPlains/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_53)
    entryname: data/SavMIP_stats/LPJGUESS/HowardSprings/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_54)
    entryname: data/SavMIP_stats/LPJGUESS/AdelaideRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_55)
    entryname: data/SavMIP_stats/LPJGUESS/DalyUncleared/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_56)
    entryname: data/SavMIP_stats/LPJGUESS/DryRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_57)
    entryname: data/SavMIP_stats/LPJGUESS/SturtPlains/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_58)
    entryname: data/SavMIP_stats/MAESPA/HowardSprings/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_59)
    entryname: data/SavMIP_stats/MAESPA/AdelaideRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_60)
    entryname: data/SavMIP_stats/MAESPA/DalyUncleared/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_61)
    entryname: data/SavMIP_stats/MAESPA/DryRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_62)
    entryname: data/SavMIP_stats/MAESPA/SturtPlains/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_63)
    entryname: data/SavMIP_stats/SPA/HowardSprings/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_64)
    entryname: data/SavMIP_stats/SPA/AdelaideRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_65)
    entryname: data/SavMIP_stats/SPA/DalyUncleared/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_66)
    entryname: data/SavMIP_stats/SPA/DryRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_67)
    entryname: data/SavMIP_stats/SPA/SturtPlains/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_68)
    entryname: data/SavMIP_stats/CABLE/HowardSprings/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_69)
    entryname: data/SavMIP_stats/CABLE/AdelaideRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_70)
    entryname: data/SavMIP_stats/CABLE/DalyUncleared/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_71)
    entryname: data/SavMIP_stats/CABLE/DryRiver/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_72)
    entryname: data/SavMIP_stats/CABLE/SturtPlains/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_73)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_74)
    entryname: data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_75)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_76)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_77)
    entryname: data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_78)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_79)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_80)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_81)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_82)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_83)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/HowardSprings/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_84)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/AdelaideRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_85)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_86)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DryRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_87)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/SturtPlains/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_88)
    entryname: data/VOM_output/additional_analyses/fixed_roots/HowardSprings/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_89)
    entryname: data/VOM_output/additional_analyses/fixed_roots/AdelaideRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_90)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_91)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_92)
    entryname: data/VOM_output/additional_analyses/fixed_roots/SturtPlains/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_93)
    entryname: data/SavMIP_stats/BESS/HowardSprings/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_94)
    entryname: data/SavMIP_stats/BESS/AdelaideRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_95)
    entryname: data/SavMIP_stats/BESS/DalyUncleared/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_96)
    entryname: data/SavMIP_stats/BESS/DryRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_97)
    entryname: data/SavMIP_stats/BESS/SturtPlains/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_98)
    entryname: data/SavMIP_stats/BIOS2/HowardSprings/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_99)
    entryname: data/SavMIP_stats/BIOS2/AdelaideRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_100)
    entryname: data/SavMIP_stats/BIOS2/DalyUncleared/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_101)
    entryname: data/SavMIP_stats/BIOS2/DryRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_102)
    entryname: data/SavMIP_stats/BIOS2/SturtPlains/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_103)
    entryname: data/SavMIP_stats/LPJGUESS/HowardSprings/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_104)
    entryname: data/SavMIP_stats/LPJGUESS/AdelaideRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_105)
    entryname: data/SavMIP_stats/LPJGUESS/DalyUncleared/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_106)
    entryname: data/SavMIP_stats/LPJGUESS/DryRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_107)
    entryname: data/SavMIP_stats/LPJGUESS/SturtPlains/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_108)
    entryname: data/SavMIP_stats/MAESPA/HowardSprings/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_109)
    entryname: data/SavMIP_stats/MAESPA/AdelaideRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_110)
    entryname: data/SavMIP_stats/MAESPA/DalyUncleared/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_111)
    entryname: data/SavMIP_stats/MAESPA/DryRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_112)
    entryname: data/SavMIP_stats/MAESPA/SturtPlains/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_113)
    entryname: data/SavMIP_stats/SPA/HowardSprings/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_114)
    entryname: data/SavMIP_stats/SPA/AdelaideRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_115)
    entryname: data/SavMIP_stats/SPA/DalyUncleared/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_116)
    entryname: data/SavMIP_stats/SPA/DryRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_117)
    entryname: data/SavMIP_stats/SPA/SturtPlains/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_118)
    entryname: data/SavMIP_stats/CABLE/HowardSprings/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_119)
    entryname: data/SavMIP_stats/CABLE/AdelaideRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_120)
    entryname: data/SavMIP_stats/CABLE/DalyUncleared/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_121)
    entryname: data/SavMIP_stats/CABLE/DryRiver/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_122)
    entryname: data/SavMIP_stats/CABLE/SturtPlains/ass_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
