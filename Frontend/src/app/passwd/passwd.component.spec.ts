import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PasswdComponent } from './passwd.component';

describe('PasswdComponent', () => {
  let component: PasswdComponent;
  let fixture: ComponentFixture<PasswdComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PasswdComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PasswdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
