# R070BIO

## Descrição

Template Biometria

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodTBi | Number(002,0) | Não | Código da Tecnologia Biométrica |
| TipTem | Number(001,0) | Não | Tipo de template |
| TemBio | Image | Sim | Template biométrica |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DatCol | Date | Sim | Data da Coleta da Template |
| HorCol | Number(005,0) | Sim | Hora da Coleta da Template |
| CarBio | String(001) | Sim | Carrega Biometria na Memória |
| Integr | String(001) | Sim | Template biométrica integrada com o Ronda senior X |

---

## Chave Primária

- IdtPes
- CodTBi
- TipTem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
