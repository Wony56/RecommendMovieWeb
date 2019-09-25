<template>
    <v-container>
        <v-card style="margin-top:100px;" outlined>
            <v-col class="py-0">
                <v-row >
                    <v-flex xs4 md4 sm4>
                        <v-card flat height="180" class="text-center align-center">
                            Photo
                        </v-card>
                    </v-flex>
                    <v-flex xs8 md4 sm4 style="padding-left:20px;">
                        <v-card-text style="background-color:#ff2f6e; color:#fff;" class="text-center title font-weight-black py-0">
                            Profile
                        </v-card-text>
                        <v-card-text style="padding-top:10px;">
                            <p>UserName : 류호진</p>
                            <p>Age : 30</p>
                            <p>Occupation : 프로그래머</p>
                        </v-card-text>
                    </v-flex>
                    <v-flex xs12 md4 sm4>
                        <v-card-text>
                            <p>Sex : Male</p>
                            <p>SubScirbe : True</p>
                            <span>SubScribe term : 2019.09.25~2019.09.28</span><v-btn style="margin-left:10px; margin-top:-5px" text x-small color="#ff2f6e">기간 연장</v-btn>
                            <!--<v-btn style="margin-left:10px; margin-top:-5px" text x-small color="#ff2f6e">해지</v-btn>
                            <v-btn style="margin-left:10px; margin-top:-5px" text x-small color="#ff2f6e">구독</v-btn>-->
                            <v-btn style="margin-top:15px" outlined color="#ff2f6e" block>회원 정보 수정</v-btn>
                        </v-card-text>
                    </v-flex>
                </v-row>
                <v-row>
                    <v-flex xs12>
                        <v-card-text style="background-color:#ff2f6e; color:#fff;" class="text-center py-1">
                            Like Genre
                        </v-card-text>
                    </v-flex>
                </v-row>
                <v-row>
                    <v-flex xs12>
                        <v-card flat height="180">
                        </v-card>
                    </v-flex>
                </v-row>
                <v-row>
                    <v-flex xs12>
                        <v-card-text style="background-color:#ff2f6e; color:#fff;" class="text-center py-1">
                            Movie
                        </v-card-text>
                    </v-flex>
                </v-row>
                <v-row>
                    <v-flex xs12>
                        <v-card flat height="180">

                        </v-card>
                    </v-flex>
                </v-row>
            </v-col>
        </v-card>
    </v-container>
</template>
