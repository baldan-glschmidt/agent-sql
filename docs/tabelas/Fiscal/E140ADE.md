# E140ADE

## Descrição

Vendas - Ações do Documento Eletronico

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| AbrNfv | String(1000) | Sim | Abrangência de Notas |
| TipAde | String(100) | Sim | Tipo da Ação do Documento Eletrônico |
| SimEmi | String(001) | Sim | Indicativo se deve Simular a Emissão. |
| RotOri | String(100) | Sim | Rotina de Origem |
| SitIex | String(001) | Sim | Situação do processamento da pendência de integração |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatExe | Date | Sim | Data de execução da primeira tentativa de movimentação |
| HorExe | Number(005,0) | Sim | Hora da execução da primeira tentativa de movimentação |
| QtdTtv | Number(004,0) | Sim | Quantidade total de tentativas de movimentação já efetuadas |
| QtdTat | Number(004,0) | Sim | Quantidade de tentativas desde que foi zerado o contador |
| MsgErr | String(998) | Sim | Mensagem de erro ocorrida no processamento |

---

## Chave Primária

- IdeUni

---

## Índices

### E140ADESituacao

**Tipo:** Não unico

Campos:
- IdeUni
- SitIex

### E140ADENotaFiscal

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- AbrNfv

### E140ADEDataGeracao

**Tipo:** Não unico

Campos:
- DatGer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
