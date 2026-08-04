# E075PIC

## Descrição

Cadastros - Produtos - Informações Complementares

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| EcoIid | String(001) | Sim | Emitir Contra Nota |
| ConSig | String(001) | Sim | Produto considerado na geração de arquivo para Siga |
| CodNfc | String(007) | Sim | Código item cClass |
| IntHry | String(001) | Sim | Integra com o Hub de Royalties |
| CalFus | String(001) | Sim | Calcula FUST |
| AliFus | Number(005,2) | Sim | Percentual FUST |
| CalFnt | String(001) | Sim | Calcula FUNTTEL |
| AliFnt | Number(005,2) | Sim | Percentual FUNTTEL |
| FinCib | String(003) | Sim | Aplicação da CBS/IBS |

---

## Chave Primária

- CodEmp
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075PIC_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

