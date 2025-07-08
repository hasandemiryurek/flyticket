package com.example.myapplication // Sizin package adınızla aynı olmalı

import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.viewpager2.adapter.FragmentStateAdapter

class ViewPagerAdapter(fragmentActivity: FragmentActivity) : FragmentStateAdapter(fragmentActivity) {

    // Gösterilecek Fragment'ların listesi
    private val fragments = arrayListOf<Fragment>(
        ForYouFragment(),
        ExploreFragment(),
        ExperiencesFragment()
    )

    // Toplam sekme sayısı
    override fun getItemCount(): Int {
        return fragments.size
    }

    // Belirli bir pozisyondaki Fragment'ı döndürür
    override fun createFragment(position: Int): Fragment {
        return fragments[position]
    }
}