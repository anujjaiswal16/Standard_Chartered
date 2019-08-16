provider "aws" {
  region = "us-east-1"
}

resource "aws_elb" "SC-Web-LB" {
  name               = "SC-Web-LB"
  security_groups    = ["sg-4d75c030"]
  availability_zones = ["us-east-1b","us-east-1a"] 
  listener {
    lb_port           = 80
    lb_protocol       = "http"
    instance_port     = 5000
    instance_protocol = "http"
  } 
  health_check {
    target              = "HTTP:80/"
    interval            = 30
    timeout             = 3
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }  
}

resource "aws_autoscaling_group" "SC-ASG" {
  launch_configuration = aws_launch_configuration.SC-LC.id
  availability_zones   = ["us-east-1b","us-east-1a"]
  min_size = 2
  max_size = 2
  load_balancers    = [aws_elb.SC-Web-LB.name]
  health_check_type = "ELB"

}


resource "aws_launch_configuration" "SC-LC" {
  image_id        = "ami-0baecc89d0c94bd66"
  instance_type   = "t2.micro"
  security_groups = ["sg-4d75c030"]
  lifecycle {
    create_before_destroy = true
  }
}

