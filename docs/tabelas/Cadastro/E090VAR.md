# E090VAR

## Descrição

Integrações - Varejo - Parâmetros de representante (vendedor)

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodRep | Number(009,0) | Não | Código do representante |
| CarRep | String(020) | Sim | Identificação do cartão do representante para utilização no sistema de varejo |
| PerDmi | Number(005,2) | Sim | Percentual de desconto máximo por item no cupom fiscal |
| PerDmt | Number(005,2) | Sim | Percentual de desconto máximo no total do cupom fiscal |
| PrfUsu | Number(009,0) | Não | Perfil do usuário no sistema de varejo |
| SitReg | String(001) | Não | Situação do registro |
| RepPdi | Date | Sim | Período inicial de validade para o vínculo com a filial |
| RepPdf | Date | Sim | Período final de validade para o vínculo com a filial |
| CatRep | String(003) | Sim | Categoria do Representante |
| PerCom | Number(005,2) | Sim | Percentual de comissão padrão para o representante na filial |

---

## Chave Primária

- CodEmp
- CodFil
- CodRep

---

## Índices

### E090VARIndice1

**Tipo:** Não unico

Campos:
- CodRep

---

## Relacionamentos

### IR_E090VAR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E090VAR_002

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

