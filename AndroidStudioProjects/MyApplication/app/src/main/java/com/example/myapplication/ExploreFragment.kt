package com.example.myapplication

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.GridLayoutManager // Bu import'u ekleyin
import androidx.recyclerview.widget.RecyclerView // Bu import'u ekleyin

class ExploreFragment : Fragment() { // Sınıf isminin ExploreFragment olduğuna dikkat edin

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_explore, container, false) // fragment_explore olduğuna dikkat

        val recyclerView: RecyclerView = view.findViewById(R.id.experiences_recycler_view)

        // Örnek ürün verileri oluştur (Resim ID'leri burada önemlidir!)
        // Örnek resim verileri oluştur (Resim ID'leri burada önemlidir!)
        val imageList = arrayListOf(
            R.drawable.insan_1,
            R.drawable.insan_2,
            R.drawable.insan_3,
            R.drawable.insan_4,
            R.drawable.insan_5,
            R.drawable.insan_6,
            R.drawable.insan_7,
            R.drawable.insan_8,
            R.drawable.insan_9,
            R.drawable.insan_10,
            R.drawable.insan_11,
            R.drawable.insan_12,
            R.drawable.insan_13,
            R.drawable.insan_14,
            R.drawable.insan_15,
            R.drawable.insan_16,
            R.drawable.insan_17,
            R.drawable.insan_18
        )

// Yeni ImageAdapter'ımızı kullanıyoruz
        val imageAdapter = ImageAdapter(imageList)
        recyclerView.adapter = imageAdapter

// LayoutManager'ı (grid) ayarlayalım, her satırda 3 resim olacak
        recyclerView.layoutManager = GridLayoutManager(context, 3)


        return view
    }
}