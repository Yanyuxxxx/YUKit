//
//  YUKitColor.h
//  YUKit
//
//  Created by Yanyuxxxx on 2018/7/16.
//  Copyright © 2018年 Yanyuxxxx. All rights reserved.
//

#ifndef YUKitColor_h
#define YUKitColor_h

// rgb颜色转换（16进制 -> 10进制）
#define HexColor(rgbValue) [UIColor colorWithRed:((float)((rgbValue & 0xFF0000) >> 16))/255.0 green:((float)((rgbValue & 0xFF00) >> 8))/255.0 blue:((float)(rgbValue & 0xFF))/255.0 alpha:1.0]

#endif /* YUKitColor_h */
