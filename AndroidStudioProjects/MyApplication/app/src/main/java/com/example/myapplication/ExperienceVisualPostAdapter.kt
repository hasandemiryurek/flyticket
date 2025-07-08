package com.example.myapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import androidx.recyclerview.widget.RecyclerView

// Bu adapter, ExperienceVisualPost nesnelerinin listesini alır
class ExperienceVisualPostAdapter(private val postList: List<ExperienceVisualPost>) :
    RecyclerView.Adapter<ExperienceVisualPostAdapter.PostViewHolder>() {

    // Her bir deneyim postu öğesinin (item) görünümünü tutan sınıf
    class PostViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val postImageView: ImageView = itemView.findViewById(R.id.image_experience_post) // item_experience_visual_post.xml'deki ImageView ID'si
    }

    // RecyclerView'ın her bir yeni görünüm oluşturması gerektiğinde çağrılır
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PostViewHolder {
        // item_experience_visual_post.xml layout dosyasını kullanarak görünümü oluştururuz
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_experience_visual_post, parent, false)
        return PostViewHolder(view)
    }

    // Belirli bir pozisyondaki veriyi (ExperienceVisualPost) görünüme (ViewHolder) bağlar
    override fun onBindViewHolder(holder: PostViewHolder, position: Int) {
        val currentPost = postList[position] // Listedeki mevcut postu alırız

        // Resim ID'sini ImageView'a ayarlarız
        holder.postImageView.setImageResource(currentPost.imageResId)
    }

    // Adapter'ın yönettiği toplam öğe sayısını döndürür (yani post listesinin boyutu)
    override fun getItemCount(): Int {
        return postList.size
    }
}