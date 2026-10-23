# R346ADV

## Descrição

eSocial JR - Informações de Tributos - Identificação dos advogados

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CmpPag | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| CodRec | Number(006,0) | Não | Código de Receita - CR relativo a Imposto de Renda Retido na Fonte |
| TipIns | Number(001,0) | Não | Tipo Inscrição |
| NumIns | Number(014,0) | Sim | Número de Inscrição - Obsoleto |
| CfjIns | String(014) | Não | Número de Inscrição |
| VlrAdv | Number(015,2) | Sim | Valor das despesas com advogados, se houver |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- CodRec
- TipIns
- CfjIns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
