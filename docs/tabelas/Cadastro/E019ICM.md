# E019ICM

## Descrição

Tabelas - ICMS Especial - Por Estado

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTic | String(003) | Não | Código do tipo de ICMS especial |
| SigUfs | String(002) | Não | Sigla do estado |
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IcmSco | Number(004,2) | Sim | Percentual de ICMS especial para saída contribuinte |
| IcmSnc | Number(004,2) | Sim | Percentual de ICMS especial para saída não contribuinte |
| IcmEco | Number(004,2) | Sim | Percentual de ICMS especial para entrada contribuinte |
| IcmEnc | Number(004,2) | Sim | Percentual de ICMS especial para entrada não contribuinte |
| CodMsg | Number(004,0) | Sim | Código da mensagem associada ao ICMS especial |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 associada ao ICMS especial |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 associada ao ICMS especial |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 associada ao ICMS especial |

---

## Chave Primária

- CodTic
- SigUfs
- CodEmp
- CodFil

---

## Índices

### E019ICMIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E019ICM_000

**Tabela:** E019TIC

| Origem | Destino |
|--------|---------|
| CodTic | CodTic |

### IR_E019ICM_001

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

