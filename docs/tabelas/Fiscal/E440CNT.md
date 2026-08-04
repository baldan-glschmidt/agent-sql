# E440CNT

## Descrição

Compras - Contagens de produtos - Dados Gerais

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumCnt | Number(009,0) | Não | Número da contagem |
| SitCnt | Number(001,0) | Sim | Situação da contagem |
| ObsCnt | String(250) | Sim | Texto da observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da contagem |
| DatGer | Date | Sim | Data da geração da contagem |
| HorGer | Number(005,0) | Sim | Hora da geração da geração da contagem |
| CodFor | Number(009,0) | Sim | Fornecedor da nota fiscal de entrada da contagem(Quando a contagem foi gerada automática) |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada da contagem  (Quando a contagem foi gerada automática) |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de entrada da contagem  (Quando a contagem foi gerada automática) |

---

## Chave Primária

- CodEmp
- CodFil
- NumCnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
