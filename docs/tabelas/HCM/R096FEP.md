# R096FEP

## Descrição

Epi - Fornecedores - Certificações

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEpi | Number(008,0) | Não | Código do Epi |
| CodOem | Number(008,0) | Não | Código do Fornecedor |
| DatCer | Date | Não | Data da certificação |
| CerApr | String(020) | Sim | Certificado de Aprovação |
| DatVal | Date | Sim | Data de validade da certificação |
| DatIni | Date | Sim | Data de início de fornecimento |
| DatFim | Date | Sim | Data de término de fornecimento |
| EmpFil | Number(006,0) | Sim | Empresa Filial (Obsoleto) |
| AbrFil | String(100) | Sim | Abrangência de Filial (Obsoleto) |

---

## Chave Primária

- CodEpi
- CodOem
- DatCer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096FEP_000

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

### IR_R096FEP_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

