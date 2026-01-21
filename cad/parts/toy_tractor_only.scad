// Toy Tractor - Tractor Only
// Original: toys_tractor.scad
// Modified to show just the tractor without attachments

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

module tractor(){
    x=13;
    translate([0,x,8])tractor_body();
    for(i=[0,1]){
        mirror([i,0,0])translate([31/2,x,12])rotate([0,90,0])roue(25,6);
        mirror([i,0,0])translate([31/2,40+x,10])rotate([0,90,0]) roue(20,5);
    }
}

// Just the tractor!
tractor();
