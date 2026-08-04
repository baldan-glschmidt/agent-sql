# E034TXE

## Descrição

Tabelas - Tipos de Contas X  Eventos

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTcc | String(003) | Não | Código do tipo de conta |
| CodEtc | Number(004,0) | Não | Código do Evento |
| DesEtc | String(050) | Sim | Descrição Evento |
| DesTcc | String(030) | Sim | Descrição do tipo de conta |
| EveEnc | String(001) | Não | Evento encerramento? |
| AplTcc | Number(002,0) | Não | Aplicação do tipo da conta |
| SitTxe | String(001) | Não | Indicativo do evento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |

---

## Chave Primária

- CodEmp
- CodTcc
- CodEtc

---

## Índices

### E034TXEIndice1

**Tipo:** Não unico

Campos:
- CodTcc

### E034TXEIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodEtc

---

## Relacionamentos

### IR_E034TXE_001

**Tabela:** E034TCC

| Origem | Destino |
|--------|---------|
| CodTcc | CodTcc |

### IR_E034TXE_002

**Tabela:** E034ETC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtc | CodEtc |

