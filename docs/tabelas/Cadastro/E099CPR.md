# E099CPR

## Descrição

Cadastros - Usuários - Cotas de Compra por Competência

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do usuário |
| DEmitR | String(001) | Sim | Documento que o usuário pode emitir no recebimento |
| AltCtr | String(001) | Sim | Alterar Seleção Contrato de compra no recebimento |
| AltPdt | String(001) | Sim | Permitir a alteração de produto e classificação do ticket |
| AutMde | String(001) | Sim | Permitir efetuar a Manifestação do Destinatário |
| PerAgr | String(001) | Sim | Permite Agrupamento de Cargas |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099CPR_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

