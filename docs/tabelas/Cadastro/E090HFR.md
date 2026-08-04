# E090HFR

## Descrição

Cadastros - Representantes - Hierarquia de Funções

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CatRep | String(003) | Não | Categoria do representante |
| NivCat | Number(001,0) | Não | Nível  da categoria do representante |
| DesCat | String(030) | Não | Descrição do nível |
| PerCom | Number(005,2) | Sim | Percentual de comissão a ser pago no nível |
| PerPco | Number(005,2) | Sim | Percentual de participação de comissão dos níveis mais baixos |
| PerRed | Number(005,2) | Sim | Percentual redutor de comissão a ser pago no nível |
| CatSup | String(003) | Sim | Categoria superior |
| ParMet | String(001) | Sim | Indicativo se esta função participa da meta de vendas. |
| CatBas | String(001) | Sim | Indicativo se esta função representa a função base para as metas |

---

## Chave Primária

- CodEmp
- CodFil
- CatRep
- NivCat

---

## Índices

### E090HFRIndice2

**Tipo:** Não unico

Campos:
- CodEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
