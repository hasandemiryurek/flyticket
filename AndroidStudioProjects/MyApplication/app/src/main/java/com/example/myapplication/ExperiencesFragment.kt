package com.example.myapplication

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ExperiencesFragment : Fragment() {
    // Bu satır zaten var olmalıydı, Fragment sınıfının başlangıcı

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // fragment_experiences.xml layout dosyasını şişiriyoruz
        val view = inflater.inflate(R.layout.fragment_experiences, container, false)

        val recyclerView: RecyclerView = view.findViewById(R.id.experiences_recycler_view)

        // --- İki Adet Görsel Deneyim Postu Verisi Oluşturma ---
        // Buraya daha önce drawable klasörünüze eklediğiniz resimlerin ID'lerini yazın.
        // Örnek: R.drawable.experience_post_1 ve R.drawable.experience_post_2
        val visualExperiencePosts = arrayListOf(
            ExperienceVisualPost(R.drawable.experience_post_1), // İlk post görselinizin ID'si
            ExperienceVisualPost(R.drawable.experience_post_2)  // İkinci post görselinizin ID'si
        )
        // --- Görsel Deneyim Verileri Sonu ---

        // Oluşturduğumuz ExperienceVisualPostAdapter'ı kullanıyoruz
        val adapter = ExperienceVisualPostAdapter(visualExperiencePosts)
        recyclerView.adapter = adapter

        // RecyclerView için dikey bir liste (LinearLayoutManager) kullanıyoruz
        // Bu, postları alt alta sıralayacak.
        recyclerView.layoutManager = LinearLayoutManager(context)

        // Not: "Share your experiences" kısmı için ekstra bir Kotlin kodu gerekmez
        // Çünkü bu sadece bir TextView ve XML'de tanımlandı.

        return view
    }
}