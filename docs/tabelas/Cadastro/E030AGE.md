# E030AGE

## Descrição

Cadastros - Bancos - Agências

---

## Resumo

- Campos: 23
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodAge | String(007) | Não | Código da agência do banco |
| NomAge | String(030) | Não | Nome da agência do banco |
| AbrAge | String(010) | Não | Sigla da agência do banco |
| EndAge | String(100) | Sim | Endereço da agência do banco |
| BaiAge | String(075) | Sim | Bairro da agência do banco |
| CplAge | String(050) | Sim | Complemento da agência do banco  (sala, andar, etc.) |
| CepAge | Number(008,0) | Sim | Cep da agência do banco |
| CidAge | String(060) | Sim | Município da agência do banco |
| SigUfs | String(002) | Sim | Sigla do estado da agência do banco |
| CtoAge | String(030) | Sim | Nome da pessoa de contato na agência do banco |
| FonAge | String(020) | Sim | Número do telefone da agência do banco |
| FaxAge | String(020) | Sim | Número do FAX da agência do banco |
| CxaPst | Number(006,0) | Sim | Número da caixa postal da agência do banco |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| CodSup | String(007) | Sim | Código da superintendência da agência |
| NomGer | String(050) | Sim | Nome do gerente da agência |
| RgeGer | String(013) | Sim | Número do documento de identidade (RG) do gerente da agência |
| OrgGer | String(005) | Sim | Órgão emissor do RG do gerente da agência |
| EscGer | Number(001,0) | Sim | Estado civil do gerente da agência |
| CpfGer | Number(012,0) | Sim | CPF do gerente da agência |
| EenAge | String(018) | Sim | Código do endereço da agência |
| CodPai | String(004) | Sim | Código do país da agência |

---

## Chave Primária

- CodBan
- CodAge

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E030AGE_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

