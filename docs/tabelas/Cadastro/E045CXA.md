# E045CXA

## Descrição

Tabelas - Plano Contábil - Relacionamento Contas X Cta. Auxiliar

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaRed | Number(007,0) | Não | Conta contábil reduzida |
| CtaAux | Number(009,0) | Não | Número reduzido da conta auxiliar |
| CriCxc | Number(001,0) | Não | Critério para relacionamento (1 = Só ele, 2 = Todas subordinadas a ele) |
| TipCta | Number(001,0) | Sim | Indica o tipo de relacionamento para criação automática de conta auxiliar |
| IncCta | String(001) | Não | Indicativo se deve incrementar o código da auxiliar relacionada ao gerar a nova |
| ObsCxc | String(250) | Sim | Observação do relacionamento |
| SitCxc | String(001) | Não | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |
| IdeDcm | Number(009,0) | Não | Identificador de Código de Desbobramento |

---

## Chave Primária

- CodEmp
- CtaRed
- CtaAux

---

## Índices

### E045CXAIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CtaRed
- CtaAux
- CriCxc
- SitCxc

### E045CXA_FKIndex1

**Tipo:** Não unico

Campos:
- IdeDcm

---

## Relacionamentos

### IR_E045CXA_001

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaRed | CtaRed |

