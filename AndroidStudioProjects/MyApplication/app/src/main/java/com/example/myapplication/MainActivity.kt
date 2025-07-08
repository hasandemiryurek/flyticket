package com.example.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.myapplication.databinding.ActivityMainBinding
import com.google.android.material.tabs.TabLayoutMediator // Bu import'u ekleyin

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        ViewCompat.setOnApplyWindowInsetsListener(binding.root) { view, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            view.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // Header'daki butonlara tıklama dinleyicileri (önceki adımdan)
        binding.backButton.setOnClickListener { /* ... */ }
        binding.searchEditText.setOnClickListener { /* ... */ }
        binding.notificationIcon.setOnClickListener { /* ... */ }
        binding.shoppingCartIcon.setOnClickListener { /* ... */ }

        // --- Yeni Eklenecek Kodlar ---

        // 1. ViewPager2 için Adaptörü oluşturun
        val viewPagerAdapter = ViewPagerAdapter(this)
        binding.viewPager.adapter = viewPagerAdapter

        // 2. Sekme başlıklarını tanımlayın
        val tabTitles = arrayListOf("For You", "Explore", "Experiences")

        // 3. TabLayout'ı ViewPager2 ile bağlayın
        TabLayoutMediator(binding.tabLayout, binding.viewPager) { tab, position ->
            tab.text = tabTitles[position]
        }.attach()
    }
}