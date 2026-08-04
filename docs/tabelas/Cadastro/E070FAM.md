# E070FAM

## Descrição

Cadastros - Filiais - Parâmetros por Família

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFam | String(006) | Não | Código da Família do Produto |
| MoeOsc | String(003) | Sim | Código da moeda padrão para ordens de compra sem contrato de participantes e NF de depósito |
| PerOsc | Number(005,2) | Sim | Percentual da moeda padrão para geração das NFs de depósito |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| PreMin | Number(009,5) | Sim | Preço Mínimo para Compra |

---

## Chave Primária

- CodEmp
- CodFil
- CodFam

---

## Índices

### E070FAMIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFam

---

## Relacionamentos

### IR_E070FAM_002

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

