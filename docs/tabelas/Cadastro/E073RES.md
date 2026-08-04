# E073RES

## Descrição

Cadastros - Transportadoras - Reserva de Veículos

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| PlaVei | String(010) | Não | Placa do veículo |
| DatRes | Date | Não | Data da reserva do veículo |
| CodRoe | String(003) | Não | Código da rota ou localidade |
| UsuRes | Number(009,0) | Não | Usuário responsável pela reserva do veículo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodTra
- PlaVei
- DatRes
- CodRoe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
