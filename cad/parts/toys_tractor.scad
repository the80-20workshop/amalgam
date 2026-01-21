r = 20.2;
cube_l = 7;
cube_h = 3;

h = 10;
l = 50;

e = 4;

essieu_r=3;
$fs=$fs/2;
$fa=$fa/2;

module cran_pneu(d, e, nb){
    difference(){
        union(){
            for(i= [0:18]){
                rotate([0,0,i*20]) translate([-(d/2+1),0,-1]) rotate([30,22,00])cube([2,0.8,e+1]);
            }
        }
        translate([0,0,-10]) cylinder(10, r=d);
        translate([0,0,e/2+0.5])  cylinder(10, r=d);
    }
}

module roue(d, e, cran=true){
    rotate_extrude(){
        translate([d/2-e/2,0,0]) scale([1,1.2]) circle (e/2);
    }
    if(cran){
        cran_pneu(d, e);
        rotate([0,0,10])mirror([0,0,1]) cran_pneu(d, e);
    }
    difference(){
        translate([0,0,-0.5])cylinder(e, r=d/2-e/2, center = true);
        cylinder(e+1, r=essieu_r+0.3, center = true);
        translate([0,0,-e/2]) cylinder(1.1,essieu_r+1,essieu_r, center = true);
    }
}

module essieu(l, d_e){
    e_r=0.8;
    difference(){
        union(){
            translate([0,0,2])rotate([0,90,0]) cylinder(l+d_e,r=essieu_r, center =true);
            translate([0,0,2])rotate([0,90,0]) cylinder(l-d_e,r=essieu_r+1, center =true);
            for(i=[0,1]){
                mirror([i,0,0])translate([l/2+d_e/2,0,2])rotate([0,90,0]) cylinder(2,essieu_r+e_r, essieu_r);
            }
        }
        translate([-l,-10,-10]) cube([2*l, 20 ,10]);
        translate([-l,-10,5]) cube([2*l, 20 ,10]);
        for(i=[0,1]){
            mirror([i,0,0])translate([l/2,0,-1]) hull(){
                translate([e_r,0,-1]) cylinder(l,r=e_r, center =true);
                translate([d_e+2,0,-1]) cylinder(l,r=e_r, center =true);
            }
        }
    }  
}

crochet_r = 2.5;
module crochet(l){
    difference(){
        union(){
            hull(){
                translate([-l/2,0,0])cube([l,1,3]);
                translate([0,-8,0])cylinder(r=4,3);
            }
            translate([0,-8,0])cylinder(r=4,7);
        }
        translate([0,-8,0])cylinder(7,2.5,3.5);
    }
}

module crochet_male(lg, l=8, support=true){
    union(){
        hull(){
            translate([-lg/2,0,8])cube([lg,1,3]);
            translate([0,-l,8])cylinder(3, r=crochet_r);
        }
        translate([0,-l,crochet_r])cylinder(10-crochet_r,r=crochet_r);
        translate([0,-l,crochet_r])sphere(crochet_r);
        if(support){
            translate([0,-l,0])cylinder(0.25,r=3);
        }
    }
}

module masse(){
    cube([1,20,10]);
}

module capot(){
    translate([-5,0,0])cube([10,30,10]);
    minkowski(){
        hull(){
            translate([0,14.5,10])cube([10,31,1], center=true);
            
            translate([0,28,15])rotate([0,90,0]) cylinder(10,r=2, center=true);
            translate([0,0,16])rotate([0,90,0]) cylinder(10,r=2, center=true);
        }
        sphere(1);
    }
}

module cabine(){
    //translate([-12,0,0])cube([24,24,35]);
    translate([-11,0,0])cube([22,24,10]);
    hull(){
        translate([-11,0,10])cube([22,24,0.1]);
        translate([-12,0,20])cube([24,24,0.1]);
    }
    hull(){
        translate([-12,0,20])cube([24,24,0.1]);
        translate([-11,2,35])cube([22,20,0.1]);
    }
    hull(){
        translate([-10.5,2.5,35])cylinder(2,r=1);;
        translate([10.5,2.5,35])cylinder(2,r=1);;
        translate([-10.5,21.5,35])cylinder(1,r=1);;
        translate([10.5,21.5,35])cylinder(1,r=1);
    }
}



module tractor_body(){
    translate([0,0,2])essieu(31, 7);
    translate([0,40,0])essieu(31, 6);
    translate([0,15,0])capot();
    translate([0,-5,0])crochet(22);
    difference(){
        translate([0,-5,0])cabine();
        translate([-31/2,0,4])rotate([0,90,0])cylinder(r=(25+4)/2,4.5);
        mirror([1,0,0])translate([-31/2,0,4])rotate([0,90,0])cylinder(r=(25+4)/2,4.5);
    }
}

module tractor(mode){
    if(mode==0){
        x=13;
        translate([0,x,8])tractor_body();
        for(i=[0,1]){
            mirror([i,0,0])translate([31/2,x,12])rotate([0,90,0])roue(25,6);
            mirror([i,0,0])translate([31/2,40+x,10])rotate([0,90,0]) roue(20,5);
        }
    }
    if(mode==1){
        translate([0,0,0])tractor_body();
        for(i=[0,1]){
            mirror([i,0,0])translate([33,0,3])roue(20,5);
            mirror([i,0,0])translate([33,30,3.6])roue(25,6);
        }
    }
    if(mode==2){
        translate([0,0,0])tractor_body();
    }
    if(mode==3){
        for(i=[0,1]){
            mirror([i,0,0])translate([14,0,3])roue(20,5);
            mirror([i,0,0])translate([14,30,3.6])roue(25,6);
        }
    }
}

//benne_l = 70;
//benne_caisse_h = 28;
//benne_lg = 33;
//benne_lg_chassi = 22;

benne_l = 60;
benne_caisse_h = 20;
benne_lg = 33;
benne_lg_chassi = 22;

module chassi(l, lg, h){
    difference(){
        translate([-lg/2,0,0])cube([lg,benne_l,11]);
        translate([0,l,8])rotate([40,0,0]) translate([-15,-30,-30]) cube([30,30,30]);
    }
    translate([0,benne_l,0]) mirror([0,1,0])crochet_male(lg);
    translate([0,10,0])essieu(31, 7);
    translate([0,32,0])essieu(31, 7);
}

module caisse(l, lg,h){
    difference(){
        translate([-lg/2,0,0])cube([lg,l,h]);
        for(i=[0,1]){
            mirror([i,0,0])translate([11,-1,0]) rotate([0,40,0]) cube([30, l+2,30]);
        }
    }
}



module benne_body(){
    chassi(benne_l, benne_lg_chassi, 11);
    translate([0,0,10])difference(){
        caisse(benne_l, benne_lg, benne_caisse_h);
        translate([0,2,2]) caisse(benne_l-4, benne_lg-4, benne_caisse_h);
    }
    //translate([0,86,0]) crochet(22);
}

module benne(mode){
    if(mode==0){
        x=-68;
        translate([0,x,8])benne_body();
        for(i=[0,1]){
            mirror([i,0,0]) translate([31/2,x+10,10])rotate([0,90,0])roue(20,6,false);
            mirror([i,0,0]) translate([31/2,x+32,10])rotate([0,90,0]) roue(20,6,false);
        
        }
    }
    if(mode==1) {
        translate([0,0,0])benne_body();
        for(i=[0,1]){
            mirror([i,0,0])translate([33,0,3.6])roue(20,6,false);
            mirror([i,0,0])translate([33,30,3.6])roue(20,6,false);
        }
    }
    if(mode==2) {
        translate([0,0,0])benne_body();
    }
    if(mode==3) {
        for(i=[0,1]){
            mirror([i,0,0])translate([13,13,3.6])roue(20,6,false);
            mirror([i,0,0])translate([13,-13,3.6])roue(20,6,false);
        }
    }
}

module dent(){
    h=19;
    hull(){
        difference(){
            translate([-5,-5,0]) cube([10,10,1]);
            for(i=[0,1]){
                 translate([0,-6,-1])  mirror([i,0,0]) rotate([0,0,-30])cube([20,20,5]);
            }
        }
        translate([-1,0,0]) cube([2,4,8]);
        
    }
    translate([-1,0,0]) cube([2,4,h]);
}

module dent2(h, i=0){
    r=4;
    hull(){
        if(i==0){
            translate([2,r-2-3,r]) rotate([20,90,0])cylinder(1, r=r, center = true);
            translate([-2,r-2+3,r]) rotate([-20,90,0])cylinder(1, r=r, center = true);
        }
        if(i>0){
            translate([1,r-2,r]) rotate([20,90,0])cylinder(1, r=r, center = true);
        }
        
        
        translate([-1,0,5]) cube([2,4,8]);
        
    }
    translate([-1,0,5]) cube([2,4,h-5]);
}

e = 16;
dechaumeur_y1 = 13;
dechaumeur_y2 = 26;
dechaumeur_y3 = 45;

module dechaumeur_body(){
    translate([0,0,8])crochet_male(30, 10, false);
    
    for(i=[-1,0,1]){
        translate([i*1.5*e-2,0,17])cube([4, dechaumeur_y3-6,2]);
    }
    
    translate([-1.5*e,0,17])cube([3*e,4,2]);
    translate([-1.5*e,dechaumeur_y1,17])cube([3*e,4,2]);
    translate([-1.9*e,dechaumeur_y2,17])cube([3.8*e,4,2]);
    
    
    translate([0,0,0]) dent();
    translate([-1*e,0,0]) dent();
    translate([1*e,0,0]) dent();
    translate([0.5*e,dechaumeur_y1,0])dent();
    translate([1.5*e,dechaumeur_y1,0])dent();
    translate([-0.5*e,dechaumeur_y1,0])dent();
    translate([-1.5*e,dechaumeur_y1,0])dent();
    translate([-1*e,dechaumeur_y2,0])dent2(19);
    translate([-1.9*e,dechaumeur_y2,0])dent2(19,1);
    translate([1*e,dechaumeur_y2,0])dent2(19);
    translate([1.9*e,dechaumeur_y2,0])mirror([1,0,0])dent2(19, 1);
    translate([-0*e,dechaumeur_y2,0])dent2(19);
    
    hull(){
        translate([0, dechaumeur_y3, 5]) rotate([0,90,0])cylinder(3*e+4,r=5, center=true);
        translate([0, dechaumeur_y3-6, 17]) rotate([0,90,0])cylinder(3*e+4,r=2, center=true);
    }
    
    //translate([-1*e,0,0])cube([2*e,4,1]);
    //translate([-1.5*e,dechaumeur_y1,0])cube([3*e,4,1]);
    //translate([-1.9*e,dechaumeur_y2,0])cube([3.8*e,4,1]);
}

module dechaumeur(mode){
    if(mode){
        translate([0,0,19]) rotate([0,180,0]) dechaumeur_body();
    } else {
        translate([0,-10,0])rotate([0,0,180]) dechaumeur_body();
    }
}

cover_crop_lg = 20;
y1 = 7;
cover_crop_essieu = 30;
y3 = 53;

module cover_crop_disque(z){
    l = 52;
    nbr = 16;
    r=5.5;
    hull(){
        translate([-l/2,-2,z])cube([l,4,2]);
    
        translate([0,0,r]) rotate([0,90,0]) cylinder(r=2, l, center=true);
    }
    for(i=[0:nbr-1]){
        translate([l/2-i*l/(nbr-1),0,r]) rotate([0,90,0]) cylinder(r=r, 1, center=true);
    }
}

module cover_crop_body(){
    translate([0,0,8])crochet_male(cover_crop_lg, 10, false);
    
    translate([-cover_crop_lg/2,0,16])cube([cover_crop_lg,59,3]);
    
    translate([0,y1,2]) rotate([0,0,20]) cover_crop_disque(15);
    //translate([0,cover_crop_essieu,6.5]) essieu(28,7);
    translate([0,cover_crop_essieu,11]) rotate([0,180,0]) essieu(28,7);
    
    translate([-cover_crop_lg/2,cover_crop_essieu-3,6.5]) cube([cover_crop_lg,6,12]);
    translate([0,y3,2]) rotate([0,0,-20]) cover_crop_disque(15);

    
    
    
}

module cover_crop(mode){
    if(mode==0){
        translate([0,-10,0])rotate([0,0,180]) cover_crop_body();
        for(i=[0,1]){
            translate([0,-10,0]) mirror([i,0,0]) translate([31/2,-cover_crop_essieu,9])rotate([0,90,0])roue(18,6,false);
        }
    } else {
        translate([0,0,19])rotate([0,180,0])cover_crop_body();
        for(i=[0,1]){
            translate([0,-10,0]) mirror([i,0,0]) translate([35,cover_crop_essieu+10,3.6])roue(18,6,false);
        }
    }
}

tractor(0);
cover_crop(0);
//benne(0);
//essieu(33);
