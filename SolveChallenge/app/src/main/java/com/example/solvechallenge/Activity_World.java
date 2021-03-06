package com.example.solvechallenge;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import com.example.solvechallenge.Leaderboard.Activity_Leaderboard;
import com.example.solvechallenge.ui.SelectCharacter.Activity_Section;

import java.util.ArrayList;

public class Activity_World extends AppCompatActivity {

    private Button enter_intro_btn ;
    private Button enter_analysis_btn ;
    private Button enter_design_btn ;
    private Button enter_testing_btn ;
    private Button enter_maintenance_btn;
    private FloatingActionButton go_back_btn;
    private Button enter_assignment_btn;
    private Button enter_leaderboard_btn;
    private Button enter_create_challenge_btn;

    private String[] worlds = Config.getWorlds();
    private ArrayList<Button> btns = new ArrayList<>();
    private int world_upperbound = App_Data.getWorld_upperbound();

    public void switchToNextActivity(View view) {
        Intent intent = new Intent(this, Activity_Section.class);
        startActivity(intent);
    }

    private void setOnClick(final Button btn, final Integer i){
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                App_Data.setWorld(i);
                App_Data.printAllData();
                switchToNextActivity(v);
            }
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_world);
        this.getSupportActionBar().hide();

        enter_leaderboard_btn = findViewById(R.id.btn_leaderboard_world);
        enter_leaderboard_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Activity_World.this, Activity_Leaderboard.class);
                startActivity(intent);
            }
        });
        enter_assignment_btn = findViewById(R.id.btn_assignment_world);
        enter_assignment_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Activity_World.this, Activity_GetTweets.class);
                startActivity(intent);
            }
        });

        enter_create_challenge_btn = findViewById(R.id.btn_challenge_world);
        enter_create_challenge_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Activity_World.this, Activity_CreateChallenge.class);
                startActivity(intent);
            }
        });

        enter_intro_btn = (Button) findViewById(R.id.btn_intro_World);
        enter_analysis_btn = (Button) findViewById(R.id.btn_analysis_World);
        enter_design_btn = (Button) findViewById(R.id.btn_design_World);
        enter_testing_btn = (Button) findViewById(R.id.btn_testing_World);
        enter_maintenance_btn = (Button) findViewById(R.id.btn_maintainance_World);
        btns.add(enter_intro_btn);
        btns.add(enter_analysis_btn);
        btns.add(enter_design_btn);
        btns.add(enter_testing_btn);
        btns.add(enter_maintenance_btn);

        go_back_btn = (FloatingActionButton) findViewById(R.id.btn_back_world);
        go_back_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Activity_World.this, Activity_SelectCharacter.class);
                startActivity(intent);
            }
        });
//        enter_maintenance_btn.setText("Test");
//        btns.get(1).setText("blabalbal");

        for ( int i = 0; i < 5; i++) {
            Button btn = btns.get(i);
            btn.setText(worlds[i]);
            if (i <= world_upperbound) {
                setOnClick(btn, i);
            } else {
//                btn.getBackground().setColorFilter(Color.GRAY, PorterDuff.Mode.ADD);
                btn.setClickable(false);
                btn.setAlpha(0.2f);

//                btn.setBackgroundColor(Color.parseColor("#ffffffff"));
            }

        }


    }
}


