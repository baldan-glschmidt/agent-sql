# R109PCM

## Descrição

PCMSO - Definição de Período

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPcm | Number(004,0) | Não | Código de identificação do PCMSO |
| DesPcm | String(040) | Sim | Descrição do PCMSO |
| DatIni | Date | Sim | Data de início do exame periódico |
| DatTer | Date | Sim | Data de término do exame periódico |
| ObsFic | String(2000) | Sim | Observações do PCMSO |
| ImgAes | Image | Sim | Imagem sobre a avaliação do estado de saúde |
| TxtAes | String(2000) | Sim | Texto sobre a avaliação do estado de saúde |
| TxtCip | String(2000) | Sim | Critérios de interpretação e planejamento das condutas |

---

## Chave Primária

- NumEmp
- CodPcm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
