# R088ACC

## Descrição

Registro de Acesso da Frota

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá do Condutor |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| SeqAcc | Number(002,0) | Não | Sequência do Registro |
| TipAcc | Number(003,0) | Sim | Tipo do Acesso |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| CodFnc | Number(002,0) | Sim | Código da Função no Acesso |
| DirAcc | String(001) | Sim | Direção do Acesso |
| CraVei | Number(012,0) | Sim | Número do Crachá do Veículo |
| PlaVei | String(010) | Sim | Placa do Veículo |
| IMGLPR | Image | Sim | Imagem LPR |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
