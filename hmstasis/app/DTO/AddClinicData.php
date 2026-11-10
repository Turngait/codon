<?php

namespace App\DTO;

final readonly class AddClinicData
{
    public function __construct(
        public string $title,
        public string $description,
        public int $user_id,
        public string $mainSite,
        public ?string $lawInfo,
        public string $mainAddress,
    ) {}
    public static function fromArray(array $data): self
    {
        return new self(
            title: $data['title'],
            description: $data['description'],
            user_id: $data['user_id'],
            mainSite: $data['main_site'],
            lawInfo: $data['law_info'] ?? null,
            mainAddress: $data['main_address'],
        );
    }
}