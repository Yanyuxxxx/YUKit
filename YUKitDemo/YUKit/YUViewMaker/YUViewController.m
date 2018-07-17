//
//  YUViewController.m
//  YUKit
//
//  Created by Yanyuxxxx on 2018/7/16.
//  Copyright © 2018年 Yanyuxxxx. All rights reserved.
//

#import "YUViewController.h"
#import "Masonry.h"

@interface YUViewController ()

@end

@implementation YUViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    UIView *sv = [UIView new];
    sv.backgroundColor = [UIColor redColor];
    [self.view addSubview:sv];
    [sv mas_makeConstraints:^(MASConstraintMaker *make) {
        make.center.equalTo(self.view);
        make.width.height.equalTo(@100);
    }];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
