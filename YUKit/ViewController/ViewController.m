//
//  ViewController.m
//  YUKit
//
//  Created by Yanyuxxxx on 2018/7/13.
//  Copyright © 2018年 Yanyuxxxx. All rights reserved.
//

#import "ViewController.h"
#import "YUKitColor.h"
#import "Masonry.h"
#import "YUViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
//    self.view.backgroundColor = HexColor(0xFF0000);
    
    
}

- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    [self presentViewController:[YUViewController new] animated:YES completion:nil];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
