package com.example.myapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView // Resim göstermek için gerekli
import androidx.recyclerview.widget.RecyclerView // RecyclerView için gerekli

// Bu adapter, integer (resim ID'si) listesi alır
class ImageAdapter(private val imageList: List<Int>) :
    RecyclerView.Adapter<ImageAdapter.ImageViewHolder>() {

    // Her bir resim öğesinin görünümünü tutan sınıf
    class ImageViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val imageView: ImageView = itemView.findViewById(R.id.item_image_view) // item_image.xml'deki ImageView'ın ID'si
    }

    // Yeni bir görünüm oluşturulduğunda çağrılır (örneğin, ilk yüklendiğinde)
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ImageViewHolder {
        // item_image.xml layout dosyasını kullanarak görünümü şişiririz
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_image, parent, false)
        return ImageViewHolder(view)
    }

    // Belirli bir pozisyondaki veriyi görünüme bağlar (resmi ayarlar)
    override fun onBindViewHolder(holder: ImageViewHolder, position: Int) {
        holder.imageView.setImageResource(imageList[position]) // Resim ID'sini ImageView'a ayarlarız
    }

    // Listedeki toplam öğe sayısını döndürür
    override fun getItemCount(): Int {
        return imageList.size
    }
}